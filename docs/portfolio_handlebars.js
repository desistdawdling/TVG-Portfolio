function () {
  var data = {
    footer: "<div>Coded by Tina Velez-Grey | @DesistDawdling</div>",
  }
  var template = Handlebars.compule(document.querySelector("#template").innerHTML)
  var complete = template(data, {
    noEscape: true,
  })
}