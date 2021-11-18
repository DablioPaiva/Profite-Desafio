const produtos = document.querySelectorAll(".produto img");

function setProduct() {
    produtos.forEach((produto) => {
        produto.setAttribute('src', '../application/view/static/img-icons/tenis.png');
    })
}
setProduct();