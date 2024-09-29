from mastodon import Mastodon
from bs4 import BeautifulSoup

from helper import read_tokens


def get_plain_text(html_content):
  soup = BeautifulSoup(html_content, 'html.parser')
  return soup.get_text()


def get_toots_after_main_toot(main_toot_id, limit=40):
  """Fetches toots that are replies to the main toot on Mastodon.

  Args:
      mastodon_client: A Mastodon client instance.
      main_toot_id: The ID of the main toot.
      limit: The maximum number of toots to fetch.

  Returns:
      A list of toots that are replies to the main toot.
  """

  mastodon_client = Mastodon(
        access_token=read_tokens('tokens.txt')['MASTODON_ACCESS_TOKEN'],
        api_base_url='https://mastodon.social'
  )

  # Fetch the context of the main toot
  response = mastodon_client.status_context(main_toot_id)

  # Get the descendants (replies) of the main toot
  toots = response["descendants"][:limit]

  for toot in toots:
    toot["content"] = get_plain_text(toot["content"])

  return toots
