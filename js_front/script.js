const server_url = "http://localhost:5000";

const button = document.getElementById("get-data-button");

const add_div = document.getElementById("add");
const sub_div = document.getElementById("sub");
const mul_div = document.getElementById("mul");
const div_div = document.getElementById("div");
const exp_div = document.getElementById("exp");


button.addEventListener("click", function() {
  const value1 = document.getElementById("value1").value;
  const value2 = document.getElementById("value2").value;

  const url_add = `${server_url}/add/${value1}/${value2}`;
  const url_sub = `${server_url}/sub/${value1}/${value2}`;
  const url_mul = `${server_url}/mul/${value1}/${value2}`;
  const url_div = `${server_url}/div/${value1}/${value2}`;
  const url_exp = `${server_url}/exp/${value1}/${value2}`;

  fetch(url_add)
    .then(response => response.json())
    .then(data => {
      add_div.innerHTML = JSON.stringify(data["result"]);
    })
    .catch(error => {
      add_div.innerHTML = "Error: " + error;
    });

  fetch(url_sub)
    .then(response => response.json())
    .then(data => {
      sub_div.innerHTML = JSON.stringify(data["result"]);
    })
    .catch(error => {
      sub_div.innerHTML = "Error: " + error;
    });

  fetch(url_mul)
    .then(response => response.json())
    .then(data => {
      mul_div.innerHTML = JSON.stringify(data["result"]);
    })
    .catch(error => {
      mul_div.innerHTML = "Error: " + error;
    });

  fetch(url_div)
    .then(response => response.json())
    .then(data => {
      div_div.innerHTML = JSON.stringify(data["result"]);
    })
    .catch(error => {
      div_div.innerHTML = "Error: " + error;
    });

  fetch(url_exp)
    .then(response => response.json())
    .then(data => {
      exp_div.innerHTML = JSON.stringify(data["result"]);
    })
    .catch(error => {
      exp_div.innerHTML = "Error: " + error;
    });
});
