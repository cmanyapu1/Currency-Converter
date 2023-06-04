
const $toresults = $("#to");
const $fromresults = $("#from");
const $amount = $("#amount");


$("#currency_convert_form").on("submit", async function(e) {

   e.preventDefault();

  const response = await axios.get("https://api.exchangerate.host/symbols")

  let symbols = response.get("symbols");
  let symbol_keys = Object.keys(symbols);

  if (!symbol_keys.includes($fromresults)) {
    $(".old").text("Not valid currency")
    }

  if (!symbol_keys.includes($toresults)) {
        $(".new").text("Not valid currency")
        }

  if (typeof $amount == 'number') {
        $(".amount").text("Not valid number")
    }
} 



//#New function with the value - Append - referred to in the next flask route