var but = document.querySelector('#button');

but.onclick = function save_result() {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        data = {
                'count': '2',
                'product_id' : '1',
                'client_name' : 'Vasya',
                'client_mail' : 'ilushamdmaa@yandex.ru',
                'date'         : 'Дата и время',
                'order_id'      : '100'

            };
        fetch('/products/',   {
               method: 'POST',
               body: JSON.stringify(data),
               headers: {
                        'X-CSRFToken': csrftoken,
                        'Accept': 'text/html',
                        'Content-Type': 'application/json',
                    }})
                .then(response => response.text())
                .catch(error => console.log(error));
    }
