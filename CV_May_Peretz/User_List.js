console.log ('User List');

fetch ('https://reqres.in/api/users?page=2').then(Response => Response.json())
.then(responeJSON => CreateUsersLIst(responeJSON.data)).catch(err => console.log(err));

function CreateUsersLIst (users){
    console.log(users)
    const curr_main = document.querySelector("main");
    for (let user of users){
        const section = document.createElement("section");
        section.innerHTML= `
        <img src = "${user.avatar}" alt = "profile picture"/>
        <div class = "user">
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href= "email:${user.email}">Email</a>
        </div>
        `;
        curr_main.appendChild(section);
    }
}