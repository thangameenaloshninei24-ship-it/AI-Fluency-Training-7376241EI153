"""Tools the agent is allowed to use, plus their JSON Schema descriptions."""

from config import CURRENCY_RATES


def get_exchange_rate(currency: str) -> str:
    """Get the value of one unit of a currency in Indian Rupees."""
    currency = currency.strip().upper()
    rate = CURRENCY_RATES.get(currency)

    if rate is not None:
        return str(rate)

    return f"Unknown currency: {currency}"


def compare_currencies(currency1: str, currency2: str) -> str:
    """Compare two currencies based on their value in Indian Rupees."""
    rate1 = CURRENCY_RATES.get(currency1.strip().upper())
    rate2 = CURRENCY_RATES.get(currency2.strip().upper())

    if rate1 is None:
        return f"Unknown currency: {currency1}"

    if rate2 is None:
        return f"Unknown currency: {currency2}"

    if rate1 > rate2:
        return f"{currency1.upper()} gives more Indian Rupees ({rate1} INR)."
    elif rate2 > rate1:
        return f"{currency2.upper()} gives more Indian Rupees ({rate2} INR)."
    else:
        return "Both currencies have the same value in Indian Rupees."


TOOL_FUNCTIONS = {
    "get_exchange_rate": get_exchange_rate,
    "compare_currencies": compare_currencies
}


# These descriptions are what the LLM reads when deciding which tool to call
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Get the value of one unit of a currency in Indian Rupees.",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency": {
                        "type": "string",
                        "description": "Currency code such as USD or KWD."
                    }
                },
                "required": ["currency"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "compare_currencies",
            "description": "Compare two currencies based on how many Indian Rupees one unit gives.",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency1": {"type": "string"},
                    "currency2": {"type": "string"}
                },
                "required": ["currency1", "currency2"]
            }
        }
    }
]


if __name__ == "__main__":
    print("get_exchange_rate('USD') ->", get_exchange_rate("USD"))
    print("get_exchange_rate('KWD') ->", get_exchange_rate("KWD"))
    print("compare_currencies('USD', 'KWD') ->",
          compare_currencies("USD", "KWD"))