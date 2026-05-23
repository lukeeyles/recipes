const amounts = document.querySelectorAll("em");
const slider = document.querySelector(".slider");
const multiplier_text = document.querySelector(".multiplier")
const multipliers = [0.25, 0.5, 1, 2, 3, 4];

function updateAmounts(index) {
    let multiplier = multipliers[index];
    original_amounts.forEach((element) => console.log(element.innerHTML))
    amounts.forEach((element,idx) => element.innerHTML=(Fraction(original_amounts[idx]).mul(multiplier)).toFraction(true));
    multiplier_text.innerHTML = multiplier;
}

slider.addEventListener("input", () => updateAmounts(slider.value));
const original_amounts = [...amounts].map(element => element.innerHTML);
console.log(original_amounts);