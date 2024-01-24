function getJSONByAPI() {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then((response) => {
        console.log(response);
        return response.json();
      })
      .then((profile) => {
        console.log(profile);
        console.log("userId: " + (profile.userId + 5));
        console.log("id: " + (profile.id + 6));
        console.log("title: " + "Quod erat demonstrandum...");
        console.log("completed: " + true);
        for (var key in profile) {
            if (profile.hasOwnProperty(key)) {
              document.getElementById("chance").innerHTML += key + " : " + profile[key] + "<br>";
            }
        }
      })
      .catch((error) => {
        console.log(error);
      })
}
getJSONByAPI()

window.onload = function () {
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(jsonData => {
        for (var key in jsonData) {
          if (jsonData.hasOwnProperty(key)) {
            document.getElementById("view").innerHTML += key + " : " + jsonData[key] + "<br>";
          }
        }
    })
    .catch(error => console.log(error));
}
