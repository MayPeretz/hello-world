function change2 (element){
    element.src='static/southamrica2.jpg';
    }
function change1 (element){
    element.src='static/try1.jpg';
}
function change3 (element){
    element.src='static/maroco2.jpg';
}
function change4 (element){
    element.src='static/maroco1.jpg';
}

function printResults(method,search) {
    console.log ('User List');
    fetch ('https://reqres.in/api/users?page=2').then(Response => Response.json())
    .then(responeJSON => createList(responeJSON.data)).catch(err => console.log(err));
    function createList(users) {
        console.log(users)
        const curr_main = document.querySelector("main");
        search = search.toLowerCase();
        for (let user of users) {
            let check = false;
            if(search.length==0) {
                check = true;
            }
            else if(method=='Email') {
                var email = `${user.email}`.toLowerCase();
                if(email.indexOf(search) != -1) {
                    check = true;
                }
            } else if(method=='Name') {
                var fname = `${user.first_name}`.toLowerCase();
                var lname = `${user.last_name}`.toLowerCase();
                if(fname.indexOf(search) != -1 || lname.indexOf(search) != -1) {
                    check = true;
                }
            }
            if(check) {
                const section = document.createElement("section");
                section.innerHTML= `
                <img src = "${user.avatar}" alt = "profile picture"/>
                <div class = "user">
                    <span>${user.first_name} ${user.last_name}</span>
                    <br>
                    <a href= "${user.email}">${user.email}</a>
                </div>
                `;
                curr_main.appendChild(section);
            }

        }
    }

}

function CreateUsersLIst (){
    console.log ('User List');
    fetch ('https://reqres.in/api/users?page=2').then(Response => Response.json())
    .then(responeJSON => CreateTheList(responeJSON.data)).catch(err => console.log(err))
    function CreateTheList (users) {
        console.log(users)
        const curr_main = document.querySelector("main");
        for (let user of users) {
            const section = document.createElement("section");
            section.innerHTML = `
            <img src = "${user.avatar}" alt = "profile picture"/>
            <div class = "user">
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a href= "${user.email}">${user.email}</a>
            </div>
            `;
            curr_main.appendChild(section);
        }
    }
}