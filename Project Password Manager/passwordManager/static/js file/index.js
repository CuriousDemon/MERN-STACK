// display model
const modelWrapper = document.querySelector(".models-wraper");
var count = 0;
if (modelWrapper) {
  function displayModel(id) {
    const model = document.getElementById(id);
    if (count == 0) {
        modelWrapper.style.display = "flex";
        model.style.display = "block";
        count++;
        // console.log(count);
    }
    const closeModel = document.getElementById("close-btn");
    //   close model
    closeModel.addEventListener("click", () => {
      modelWrapper.style.display = "none";
      model.style.display = "none";
      count--;
    });
  }
}

// copy clipboard

const copies = document.getElementById("copy")

const copy = (id)=>{
    if (id == "url") {

        var copyElement = document.getElementById("url")
    } else {
        var copyElement = document.getElementById("urlPass")
        
    }
    copyElement.select();
    navigator.clipboard.writeText(copyElement.value)
}


// prevent reload

// const signupId = document.getElementById("signupId")

// function submitForm(event) {
//   event.preventDefault();
//   var username = document.getElementById("uname").value;
//   var email = document.getElementById("email").value;
//   var password1 = document.getElementById("upass").value;
//   var password2 = document.getElementById("ucpass").value;
//   console.log(username,email,password1,password2)
// }

// signupId.addEventListener("submit",submitForm);