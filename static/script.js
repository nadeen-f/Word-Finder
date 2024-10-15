function clearResults() {
    globalThis.scrollTo({ top: 0, left: 0, behavior: "smooth" });
    document.myForm.letter_field.value = "";
    document.myForm.letter_field.focus();
    document.myForm.letter_field.setSelectionRange(0, 0);
}


