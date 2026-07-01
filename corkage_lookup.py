"""
corkage_lookup.py

Name + corkage fee for 20 well-known central London restaurants.

Corkage figures are only ever hardcoded here if they were confirmed
directly on the restaurant's OWN official website (not an aggregator,
review site, or blog). Restaurants for which no such confirmation could
be found have CONFIRMED_CORKAGE set to None -- get_corkage_info() will
ask the user for that figure instead of guessing.
"""

RESTAURANTS = [
    {
        "name": "St John (Smithfield)",
        "confirmed_corkage": "£32/bottle wine, £42 sparkling/dessert wine, "
                              "£64 magnum wine, £84 magnum Champagne",
        "source": "https://stjohnrestaurant.com/a/restaurants/smithfield",
    },
    {
        "name": "Pied à Terre",
        "confirmed_corkage": "£55 per 75cl bottle (max 2 bottles/table)",
        "source": "https://www.pied-a-terre.co.uk/faqs/",
    },
    {
        "name": "Simpson's in the Strand",
        "confirmed_corkage": "£40 1st bottle / £50 2nd bottle (still wine); "
                              "£50/£60 (Champagne); £100/£120 (magnum); "
                              "max 2 bottles or 1 magnum per table",
        "source": "https://www.simpsonsinthestrand.co.uk/visit-us/",
    },
    {"name": "Sketch", "confirmed_corkage": None, "source": None},
    {"name": "Hakkasan Mayfair", "confirmed_corkage": None, "source": None},
    {"name": "Hide", "confirmed_corkage": None, "source": None},
    {"name": "Alain Ducasse at The Dorchester", "confirmed_corkage": None, "source": None},
    {"name": "Scott's", "confirmed_corkage": None, "source": None},
    {"name": "Sexy Fish", "confirmed_corkage": None, "source": None},
    {"name": "Nobu Berkeley St", "confirmed_corkage": None, "source": None},
    {"name": "Gymkhana", "confirmed_corkage": None, "source": None},
    {"name": "Bob Bob Ricard", "confirmed_corkage": None, "source": None},
    {"name": "Kai Mayfair", "confirmed_corkage": None, "source": None},
    {"name": "Quo Vadis", "confirmed_corkage": None, "source": None},
    {"name": "The Ivy (Covent Garden)", "confirmed_corkage": None, "source": None},
    {"name": "Rules", "confirmed_corkage": None, "source": None},
    {"name": "J Sheekey", "confirmed_corkage": None, "source": None},
    {"name": "The Delaunay", "confirmed_corkage": None, "source": None},
    {"name": "Chiltern Firehouse", "confirmed_corkage": None, "source": None},
    {"name": "Berners Tavern", "confirmed_corkage": None, "source": None},
]


def get_corkage_info(restaurants=RESTAURANTS, interactive=True, ask=input):
    """
    Return a list of {"name", "corkage", "source"} for each restaurant.

    If a restaurant's corkage wasn't confirmed directly from its own
    website, and interactive=True, the user is asked for it via `ask`
    (defaults to the built-in input()) instead of a value being guessed.
    """
    results = []
    for r in restaurants:
        corkage = r["confirmed_corkage"]
        source = r["source"]
        if corkage is None:
            if interactive:
                corkage = ask(
                    f"Corkage for '{r['name']}' wasn't found on their "
                    f"official website. What is it? (leave blank if unknown): "
                ).strip() or "Unknown"
                source = "user-provided" if corkage != "Unknown" else None
            else:
                corkage = "Unknown"
        results.append({"name": r["name"], "corkage": corkage, "source": source})
    return results


def print_corkage_info(results):
    for r in results:
        line = f"{r['name']}: {r['corkage']}"
        if r["source"]:
            line += f" (source: {r['source']})"
        print(line)


if __name__ == "__main__":
    print_corkage_info(get_corkage_info())
