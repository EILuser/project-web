function regexCheck(element, regex,  errorMessage, errorMessageField) {
    if (regex.test(element.value)) {
        element.classList.remove("is-invalid");
        errorMessageField.classList.remove("invalid-feedback");
        element.classList.add("is-valid");
        errorMessageField.classList.add("valid-feedback");
        errorMessageField.innerHTML = "Верный ввод";
        return true
    }
    else {
        element.classList.remove("is-valid");
        errorMessageField.classList.remove("valid-feedback");
        element.classList.add("is-invalid");
        errorMessageField.classList.add("invalid-feedback");
        errorMessageField.innerHTML = errorMessage;
        return false
    }
}

function messagesValidator(event){
    const title = document.getElementById("form_title");
    const text = document.getElementById("form_text");

    const titleErrors = document.getElementById("title_errors");
    const textErrors = document.getElementById("text_errors");

    const titleRegex = /[^A-Za-z]{5,40}/;
    const textRegex = /[^A-Za-z]{15,1000}/;

    const titleErrorMessage = "Нельзя использовать символы латинского алфавита, длина поля должна быть от 5 до 40 символов";
    const textErrorMessage = "Нельзя использовать символы латинского алфавита, длина поля должна быть от 15 до 1000 символов";
    
    if (
        !regexCheck(title, titleRegex, titleErrorMessage, titleErrors) ||
        !regexCheck(text, textRegex, textErrorMessage, textErrors)
    ) {
        event.preventDefault();
    }
}



function MeterReadingsValidator(event) {
    const personalAccount = document.getElementById("form_pa");
    const coldWatterSupply = document.getElementById("form_cws");
    const hotWatterSupply = document.getElementById("form_hws");
    const gasSupply = document.getElementById("form_gs");
    const electricitySupply = document.getElementById("form_es");

    const paErrors = document.getElementById("pa_errors");
    const cwsErrors = document.getElementById("cws_errors");
    const hwsErrors = document.getElementById("hws_errors");
    const gsErrors = document.getElementById("gs_errors");
    const esErrors = document.getElementById("es_errors");

    const paRegex = /[\d]{9}/;
    const meterRegex = /^\d{1,5}$/;

    const paErrorMessage = "Номер лицевого счета должен содержать девять цифр (0-9)";
    const meterErrorMessage = "Показание должно быть целым числом (0-99999)";

    if (
        !regexCheck(personalAccount, paRegex, paErrorMessage, paErrors) ||
        !regexCheck(coldWatterSupply, meterRegex, meterErrorMessage, cwsErrors) ||
        !regexCheck(hotWatterSupply, meterRegex, meterErrorMessage, hwsErrors) ||
        !regexCheck(gasSupply, meterRegex, meterErrorMessage, gsErrors) ||
        !regexCheck(electricitySupply, meterRegex, meterErrorMessage, esErrors)
    ) {
        event.preventDefault();
    }
}