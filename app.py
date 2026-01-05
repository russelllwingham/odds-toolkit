import streamlit as st
from fractions import Fraction

st.title("Sports Betting Odds Converter")

# Conversion functions
def decimal_to_fractional(decimal_odds):
    frac = Fraction(decimal_odds - 1).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"

def decimal_to_american(decimal_odds):
    if decimal_odds >= 2:
        return int((decimal_odds - 1) * 100)
    else:
        return int(-100 / (decimal_odds - 1))

def decimal_to_probability(decimal_odds):
    return round((1 / decimal_odds) * 100, 2)

def american_to_decimal(american_odds):
    if american_odds > 0:
        return round((american_odds / 100) + 1, 2)
    else:
        return round((100 / abs(american_odds)) + 1, 2)

def value_percentage(odds_decimal, estimated_prob):
    return round(((odds_decimal * (estimated_prob/100)) - 1) * 100, 2)

# Streamlit interface
option = st.selectbox(
    "Choose Conversion",
    ["Decimal → Fractional & American", "American → Decimal"]
)

if option == "Decimal → Fractional & American":
    decimal = st.number_input("Decimal Odds", min_value=1.01, step=0.01)
    estimated_prob = st.number_input("Your Estimated Probability (%)", min_value=0.0, max_value=100.0, step=0.1, value=50.0)
    if decimal:
        st.write("Fractional Odds:", decimal_to_fractional(decimal))
        st.write("American Odds:", decimal_to_american(decimal))
        st.write("Implied Probability:", decimal_to_probability(decimal), "%")
        st.write("Value % (if your estimated probability is correct):", value_percentage(decimal, estimated_prob), "%")
else:
    american = st.number_input("American Odds", value=100)
    estimated_prob = st.number_input("Your Estimated Probability (%)", min_value=0.0, max_value=100.0, step=0.1, value=50.0)
    decimal = american_to_decimal(american)
    st.write("Decimal Odds:", decimal)
    st.write("Implied Probability:", decimal_to_probability(decimal), "%")
    st.write("Value % (if your estimated probability is correct):", value_percentage(decimal, estimated_prob), "%")
