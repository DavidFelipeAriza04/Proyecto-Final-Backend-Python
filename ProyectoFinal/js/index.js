const API = "http://127.0.0.1:8000/restaurants/restaurants/"
const getPersonas = async () => {
    //RESTAURANTS
    const response = await fetch(API + `?detail=1`)
    const data = await response.json()
    data.forEach(restaurant => AnadirFilaTabla(restaurant))

    //OWNERS
    response_owners = await fetch('http://127.0.0.1:8000/users/users/')
    data_owners = await response_owners.json()
    owners = document.getElementById('InputOwner')
    data_owners.forEach(owner => owners.innerHTML += `<option value="${owner.id}">${owner.first_name}</option>`)
    console.log(data)
}

function ShowAddRestaurant() {
    document.getElementById('div_agregar').classList.toggle('hidden');
    document.getElementById('div_agregar').classList.toggle('flex');
}

function AddRestaurant() {
    const name = document.getElementById('InputName').value;
    const address = document.getElementById('InputAddress').value;
    const owner = parseInt(document.getElementById('InputOwner').value);
    if (name == '' || address == '' || owner == '') {
        alert('Debe llenar todos los campos');
        return;
    }
    const restaurant = {
        name: name,
        address: address,
        owner: owner,
    }
    console.log(restaurant)
    fetch(API, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(restaurant)
    })
        .then(response => response.json())
        .then(data => {
            ShowAddRestaurant()
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function AddUser() {
    const first_name = document.getElementById('InputFirstName').value;
    const second_name = document.getElementById('InputSecondName').value;
    const email = document.getElementById('InputEmail').value;
    if (first_name == '' || second_name == '' || email == '') {
        alert('Debe llenar todos los campos');
        return;
    }
    const user = {
        first_name: first_name,
        second_name: second_name,
        email: email,
    }
    console.log(user)
    fetch("http://127.0.0.1:8000/users/users/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })
        .then(response => response.json())
        .catch((error) => {
            console.error('Error:', error);
        });
}
function DeleteRestaurant(id) {
    const idRestaurant = {
        id: id,
    }
    fetch(API + `${id}/`, {
        method: 'DELETE',
        headers: {
        },
        body: JSON.stringify(idRestaurant)
    })
        .then(response => alert("Eliminado con exito"))
        .catch((error) => {
            console.error('Error:', error);
        });

}

function AnadirFilaTabla(restaurant) {
    document.getElementById('tabla_personas').innerHTML += `
            <tr>
                <th scope="row">${restaurant.id}</th>
                <td>${restaurant.name}</td>
                <td>${restaurant.address}</td>
                <td>${restaurant.owner.first_name}  ${restaurant.owner.second_name}</td>
                <td><button type="button" class="btn btn-outline-danger" onclick="DeleteRestaurant(${restaurant.id})">Eliminar</button></td>
            </tr>
        `
}
window.addEventListener('load', () => {
    getPersonas();
});