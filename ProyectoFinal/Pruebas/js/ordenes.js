const API = "http://127.0.0.1:8000/restaurants/orders/"
const getOrdenes = async () => {
    //RESTAURANTS
    const response = await fetch(API + "?detail=1", {
        headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
        }
    })
    const data = await response.json()
    console.log(data)
    data.forEach(orden => AnadirFilaTabla(orden))
}

function AnadirFilaTabla(orden) {
    document.getElementById('tabla_personas').innerHTML += `
            <tr>
                <th scope="row">${orden.id}</th>
                <td>${orden.waiter.user.first_name}  ${orden.waiter.user.last_name}</td>
                <td>${orden.table_restaurant}</td>
                <td><button type="button" class="btn btn-outline-danger" onclick="DeleteRestaurant(${orden.id})">Eliminar</button></td>
            </tr>
        `
}

function Volver(){
    window.location.replace('API.html');
}
function CerrarSesion(){
    localStorage.removeItem('token');
    window.location.replace('login.html');
}

window.addEventListener('load', () => {
    getOrdenes();
});