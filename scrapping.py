!pip install Apify
!pip install pandas
from apify_client import ApifyClient
import pandas as pd

# Initialize the ApifyClient with your API token
client = ApifyClient("apify_api_64pvViPXrIe94mAlbhrueRBAWj0rCP0U6Gst")

# Prepare the Actor input
run_input = {
    "position": "web developer",
    "country": "US",
    "location": "San Francisco",
    "maxItems": 50,
    "parseCompanyDetails": False,
    "saveOnlyUniqueItems": True,
    "followApplyRedirects": False,
}

# Run the Actor and wait for it to finish
run = client.actor("hMvNSpz3JnHgl5jkh").call(run_input=run_input)

# Fetch Actor results and save them into a list
results = [item for item in client.dataset(run["defaultDatasetId"]).iterate_items()]

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save DataFrame to an Excel file
df.to_excel("apify_results.xlsx", index=False)

print("Results saved to apify_results.xlsx")
