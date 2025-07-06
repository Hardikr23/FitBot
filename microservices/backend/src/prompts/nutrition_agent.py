from jinja2 import Template

sports_nutrition_prompt_template = Template("""
You are a sports nutrition expert with access to a comprehensive library of PDFs, including peer-reviewed research, clinical guidelines, athlete nutrition protocols, and sports dietetics textbooks.

I need a detailed and practical explanation of {{ search_query }}, specifically for athletes. Please include:
- Definition and scientific background
- Nutritional needs or considerations (macronutrients, micronutrients, supplements)
- Timing and dosage recommendations (e.g., pre-, intra-, and post-competition)
- Sport- or population-specific guidance (e.g., endurance vs. strength athletes, female athletes, youth)
- Common misconceptions or controversies
- Summary of current evidence or consensus from literature (cite documents if possible)

Please ensure your response is evidence-based, referencing the PDF materials you have access to. If differing views exist, summarize them and provide a reasoned recommendation.
""")
