import mastodon
from mastodon import Mastodon

def get_toots_after_main_toot(mastodon_client, main_toot_id):
  """Fetches toots that come after a main toot on Mastodon.

  Args:
      mastodon_client: A Mastodon client instance.
      main_toot_id: The ID of the main toot.

  Returns:
      A list of toots that come after the main toot.
  """

  toots = []
  has_more = True
  max_id = None

  while has_more:
    options = {"limit": 40}  # Fetch 40 toots per request
    if max_id:
      options["max_id"] = max_id

    response = mastodon_client.status_context(main_toot_id, **options)

    toots.extend(response["children"])
    has_more = "next_id" in response
    max_id = response.get("next_id")

  return toots

# Replace with your Mastodon instance URL and access token
mastodon_instance = "https://your-mastodon-instance.com"
access_token = "your_access_token"

# Create a Mastodon client
mastodon_client = Mastodon(access_token=access_token, api_base_url=mastodon_instance)

# Replace with the ID of the main toot you want to get replies for
main_toot_id = "your_main_toot_id"

toots = get_toots_after_main_toot(mastodon_client, main_toot_id)

for toot in toots:
  print(toot["content"])