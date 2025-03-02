document.querySelectorAll(".btn").forEach(button => {
    button.addEventListener("click", function() {
        console.log("Кнопка нажата: ", this);

        let basketItemId = this.dataset.basketItemId; // Получаем ID товара
        let quantityInput = document.querySelector(`.quantity-input[data-basket-item-id="${basketItemId}"]`);
        let currentQuantity = parseInt(quantityInput.value);

        if (this.classList.contains("plus")) {
            increaseQuantity(basketItemId, quantityInput);
        } else if (this.classList.contains("minus")) {
            decreaseQuantity(basketItemId, quantityInput);
        }
    });
});

function increaseQuantity(basketItemId, quantityInput) {
    let currentQuantity = parseInt(quantityInput.value);
    currentQuantity += 1;
    console.log(`➕ Увеличиваем количество: item_id=${basketItemId}, new_quantity=${currentQuantity}`);
    quantityInput.value = currentQuantity;
    updateCart(basketItemId, currentQuantity);
}

function decreaseQuantity(basketItemId, quantityInput) {
    let currentQuantity = parseInt(quantityInput.value);
    if (currentQuantity > 1) {
        currentQuantity -= 1;
        console.log(`➖ Уменьшаем количество: item_id=${basketItemId}, new_quantity=${currentQuantity}`);
        quantityInput.value = currentQuantity;
        updateCart(basketItemId, currentQuantity);
    }
}


function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

function updateCart(basketItemId, currentQuantity) {
    console.log(`▶️ Начинаем обновление корзины: item_id=${basketItemId}, quantity=${currentQuantity}`);

    fetch('/basket/update_basket/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
        },
        body: JSON.stringify({
            item_id: basketItemId,
            quantity: currentQuantity
        })
    })
    .then(response => {
        console.log("🔍 Ответ от сервера получен:", response);
        if (!response.ok) {
            throw new Error(`Ошибка HTTP: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log("📩 JSON-ответ от сервера:", data);
        if (data.success) {
            console.log(`✅ Обновляем HTML: item_total_price=${data.item_total_price}, basket_total_price=${data.basket_total_price}`);

            document.querySelector(`.basket-item-total-price[data-basket-item-id="${basketItemId}"]`).textContent = data.item_total_price;
            document.getElementById("basket-total-price").textContent = "Общая сумма: " + data.basket_total_price;
        } else {
            console.warn("⚠️ Ошибка с сервера:", data.message);
            alert("Ошибка: " + data.message);
        }
    })
    .catch(error => console.error("❌ Ошибка при обновлении корзины:", error));
}
