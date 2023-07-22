import g4f
import streamlit as st


def fdm_material_assistant():
	print_object_type = st.text_input(
		"What type of object are you printing?",
		placeholder="e.g. Vase, Raspberry Pi case, ...",
		value="",
	)

	print_object_size = st.text_input(
		"Approximate object size (optional)",
		value="",
		placeholder="e.g. 50mm x 50mm x 50mm",
	)
	print_object_layer_height = st.text_input(
		"Preferred layer height (optional)", value="", placeholder="e.g. 0.2mm"
	)
	print_object_indoors_outdoors = st.radio(
		"Indoors/outdoors usage", options=["Indoors", "Outdoors", "Both"]
	)
	print_object_functional_decorative = st.radio(
		"Functional/decorative", options=["Functional", "Decorative", "Both"]
	)
	print_object_flexible = st.checkbox("Object needs to be flexible", value=False)

	print_object_extra_info = st.text_input(
		"Extra information (optional)",
		value="",
		placeholder="e.g. The print needs to be flexible, the print will be used in a car, ...",
	)

	if st.button("Suggest a material"):
		MESSAGE_PREFIX = """
		I want to 3D print an object using an FDM 3D printer. Based on the information I give, tell me what the ideal type(s) of filament would be. Some examples of filament types: PLA, PETG, TPU/TPE, ASA, Nylon, PVA, HIPS, Carbon fiber. Also consider other filament types.
		Explain your answer. Consider where the material will be used and how hot it might get. If the print might be used inside of a car it might get hot for example, so PLA would no be suitable. Also give the following recommendations for the material(s):
		- Printing temperature
		- Bed temperature
		- Extra considerations
		
		Format your answer in markdown.
		Object information:
		""".strip()

		message_info = """
			- Object type: {}
			- Object size: {}
			- Layer height: {}
			- Indoors/outdoors use: {}
			- Functional/decorative: {}
			- Object is flexible: {}
			- Extra information: {}
		""".format(
			print_object_type,
			print_object_size,
			print_object_layer_height,
			print_object_indoors_outdoors,
			print_object_functional_decorative,
			print_object_flexible,
			print_object_extra_info,
		)

		full_message = MESSAGE_PREFIX + message_info

		with st.spinner("Thinking..."):
			response = g4f.ChatCompletion.create(
				model=g4f.Model.gpt_4,
				provider=g4f.Provider.ChatgptAi,
				messages=[{"role": "user", "content": full_message}],
			)  # alterative model setting
		st.markdown(response)


if __name__ == "__main__":
	# https://docs.streamlit.io/library/api-reference/widgets

	# Page setup
	st.set_page_config(
		page_title="3D Print Assistant", page_icon="❓", layout="centered"
	)

	st.title("3D Print Assistant")

	with st.expander("FDM Material Recommendation", expanded=True):
		fdm_material_assistant()