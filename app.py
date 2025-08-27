import gradio as gr

conversion_factors = {
    ("meters", "kilometers"): 0.001,
    ("kilometers", "meters"): 1000,
    ("grams", "kilograms"): 0.001,
    ("kilograms", "grams"): 1000,
    ("seconds", "minutes"): 1/60,
    ("minutes", "seconds"): 60,
    ("hours", "minutes"): 60,
    ("minutes", "hours"): 1/60,
    ("celsius", "fahrenheit"): None,
    ("fahrenheit", "celsius"): None
}

def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if (from_unit, to_unit) in conversion_factors:
        factor = conversion_factors[(from_unit, to_unit)]
        if factor is not None:
            return round(value * factor, 4)
        else:
            if from_unit == "celsius" and to_unit == "fahrenheit":
                return round((value * 9/5) + 32, 2)
            elif from_unit == "fahrenheit" and to_unit == "celsius":
                return round((value - 32) * 5/9, 2)
    return "⚠️ Conversion not supported"

with gr.Blocks() as demo:
    gr.Markdown("## 🔄 Unit Converter App")
    with gr.Row():
        value = gr.Number(label="Enter Value")
        from_unit = gr.Dropdown(
            ["meters","kilometers","grams","kilograms","seconds","minutes","hours","celsius","fahrenheit"],
            label="From"
        )
        to_unit = gr.Dropdown(
            ["meters","kilometers","grams","kilograms","seconds","minutes","hours","celsius","fahrenheit"],
            label="To"
        )
    output = gr.Textbox(label="Converted Value")
    convert_btn = gr.Button("Convert ✅")
    convert_btn.click(convert_units, inputs=[value, from_unit, to_unit], outputs=output)

demo.launch()
