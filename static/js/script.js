
const API_BASE_URL = "http://localhost:5000/api";

$(listCupcakes)

async function listCupcakes() {

    let resp = await axios.get(`${API_BASE_URL}/cupcakes`);
    let cupcakes = resp.data.cupcakes;
    
    for(let i = 0; i < cupcakes.length; i++) {
        cupcake = cupcakes[i];
        let card = `
        <div class="col-12 col-sm-6 col-lg-4">
            <div class="card my-1">
                <img src="${cupcake.image}" class="card-img-top" alt="cupcake-image">
                <div class="card-body">
                    <h5 class="card-title">${cupcake.flavor}</h5>
                    <p class="card-text">A cupcake of size ${cupcake.size} and of rating ${cupcake.rating}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
        </div>`;
    
        $('#cupcakes-list').prepend(card);
    }
}

$('#add-cupcake-btn').on('click', handleAddCupcake)

async function handleAddCupcake(e) {

    e.preventDefault()

    let newCupcake = {
        "flavor": $('#cupcake-flavor').val(),
        "size": $('#cupcake-size').val(),
        "rating": $('#cupcake-rating').val(),
        "image": $('#cupcake-image').val()
    }

    let resp = await axios.post(`${API_BASE_URL}/cupcakes`, json=newCupcake);
    let cupcake = resp.data.cupcake;

    let card = `
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="card my-1">
            <img src="${cupcake.image}" class="card-img-top" alt="cupcake-image">
            <div class="card-body">
                <h5 class="card-title">${cupcake.flavor}</h5>
                <p class="card-text">A cupcake of size ${cupcake.size} and of rating ${cupcake.rating}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
    </div>`;

    $('#cupcakes-list').prepend(card);

}


