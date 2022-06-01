
function zakaz() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {
                'count': '2',
                'product_id' : '1',
                'client_name' : 'Vasya',
            };
        fetch('/products/1/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
                .then(response => response.text())
                .then(temp => {
                    data["date"] = temp
                })
                .catch(error => console.log(error));
    }
