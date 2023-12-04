from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json


def search_and_store_results(query, profile):
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(
        "--user-data-dir=C:\\Users\\kavit\\AppData\\Local\\Google\\Chrome\\User Data"
    )
    chrome_options.add_argument(f"--profile-directory={profile}")
    chromedriver_path = (
        "C:\\Users\\kavit\\Desktop\\chromedriver-win64\\chromedriver.exe"
    )

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to duckduckgo.com
    driver.get("https://duckduckgo.com")

    # Find the search input and input the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(query)
    search_box.submit()

    # Retrieve URLs for elements r1-0 to r1-9
    urls = []
    for i in range(10):
        selector = f"#r1-{i} > div.OQ_6vPwNhCeusNiEDcGp > div > a"
        try:
            element = driver.find_element(By.CSS_SELECTOR, selector)
            result_url = element.get_attribute("href")
            urls.append(result_url)
        except:
            urls.append(None)
    driver.quit()
    return urls


# Queries for the specified category
# queries = [
#     "Climate change: Is it a hoax or a genuine threat?",
#     "Immigration: Economic burden or cultural enrichment?",
#     "Climate change: Is it a hoax or a genuine threat?",
#     "Immigration: Economic burden or cultural enrichment?",
#     "Gun control: Protecting the Second Amendment or endangering lives?",
#     "Universal healthcare: Affordable solution or government overreach?",
#     "Income inequality: Necessary incentive for success or social injustice?",
#     "Socialism vs. Capitalism: Which system is more effective?",
#     "LGBTQ+ rights: Progress or moral decay of society?",
#     "Police reform: Addressing misconduct or undermining law enforcement?",
#     "Fake news: A genuine concern or a media conspiracy?",
#     "COVID-19 vaccines: Safe and effective or government control tools?",
#     "Election fraud: A serious issue or baseless conspiracy theories?",
# ]

# queries = [
#     "Lionel Messi's recent achievements and impact on soccer.",
#     "NBA playoffs: Highlights and updates on the Western Conference.",
#     "The dominance of Usain Bolt in sprinting events.",
#     "Cricket in India: Latest news and emerging talents.",
#     "Formula 1 Grand Prix: Insights into Lewis Hamilton's career.",
#     "WNBA's progress in promoting women's basketball.",
#     "Tom Brady's influence on American football.",
#     "Rugby in New Zealand: The All Blacks' legacy and current status.",
#     "The rise of eSports in South Korea: Top players and tournaments.",
#     "Surfing in Hawaii: World-class waves and local surf culture.",
#     "Tennis in Europe: Roland Garros and Wimbledon updates.",
# ]

# queries = [
#     "What could be causing my persistent fatigue and weakness?",
#     "Is sudden weight loss a sign of a serious health problem?",
#     "Why am I experiencing chronic headaches and migraines?",
#     "I have chest pain and shortness of breath – is it a heart issue?",
#     "What might be the cause of my ongoing digestive problems?",
#     "Should I be concerned about my persistent joint pain and stiffness?",
#     "Is my skin rash a result of an allergic reaction or a skin condition?",
#     "Could my family history of cancer increase my risk?",
#     "What are the potential causes of my recurring respiratory infections?",
#     "I have trouble sleeping – is it a sleep disorder or just stress?",
#     "Are my mood swings and anxiety symptoms of a mental health issue?",
# ]

# queries = [
#     "Quantum computing: Exploring the future of computing technology.",
#     "Artificial intelligence in healthcare: Advancements and ethical implications.",
#     "Space exploration: The significance of the James Webb Space Telescope.",
#     "5G technology: How will it transform communication and connectivity?",
#     "Nanotechnology applications in materials science and engineering.",
#     "Climate change modeling: Understanding the impact of human activities.",
#     "Biotechnology and CRISPR-Cas9: Revolutionary gene editing techniques.",
#     "Renewable energy innovations: The promise of fusion and thorium reactors.",
#     "Blockchain technology and cryptocurrencies: Beyond Bitcoin.",
#     "Astrophysics concepts: Dark matter, black holes, and the multiverse.",
#     "History of computing: From the abacus to quantum supremacy.",
# ]

# queries = [
#     "Current U.S. government budget allocation and spending priorities.",
#     "Overview of the European Union's decision-making process.",
#     "United Nations peacekeeping missions and their effectiveness.",
#     "Electoral systems around the world: Proportional representation vs. first-past-the-post.",
#     "Climate change policies in major industrialized nations.",
#     "The role of political parties in a democracy and their influence on policy-making.",
#     "Analysis of recent Supreme Court decisions in the United States.",
#     "Government surveillance and individual privacy rights: A global perspective.",
#     "Political unrest and the impact of protests on government policy.",
#     "Comparing parliamentary and presidential systems of government.",
#     "Historical examples of successful and unsuccessful diplomacy in international relations.",
# ]

queries = [
    "Best smartphones under $500 with high-quality camera.",
    "Where to find affordable kitchen appliances online?",
    "Reviews of top-rated wireless headphones for workouts.",
    "Fashion trends for fall 2023: Where to buy stylish jackets?",
    "Laptop buying guide: Which brand offers the best value for money?",
    "User experiences with budget-friendly home security cameras.",
    "Gardening tools for beginners: Recommendations and prices.",
    "Where to purchase eco-friendly cleaning products in bulk?",
    "Top-rated children's books for ages 6-8 and where to buy them.",
    "Electric car charging stations near [your location].",
    "How to choose the right gaming console for a teenager?",
]

# Run queries for the controller profile and store results as c1
controller_results_1 = search_and_store_results(queries[0], "Profile 1")

# Run queries for the tester profile and store results as t1
tester_results_1 = search_and_store_results(queries[0], "Profile 2")

# Run rest of the queries for the tester profile
tester_results_rest = []
for query in queries[1:]:
    urls = search_and_store_results(query, "Profile 2")
    tester_results_rest.append(urls)

# Run queries for the controller profile again and store results as c2
controller_results_2 = search_and_store_results(queries[0], "Profile 1")

# Run queries for the tester profile again and store results as t2
tester_results_2 = search_and_store_results(queries[0], "Profile 2")

results = {}

results["test1"] = tester_results_1
results["test2"] = tester_results_2
results["control1"] = controller_results_1
results["control2"] = controller_results_2
# Printing the results


with open("Shopping.json", "w") as file:
    json.dump(results, file, indent=4)
