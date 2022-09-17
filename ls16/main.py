goods = [
    {"name": "Pepsi", "cost": 12, "img": "./cola.jpg"}, 
    {"name": "Cola", "cost": 14, "img": "./cola.jpg"}, 
    {"name": "Sprite", "cost": 30, "img": "./cola.jpg"}, 
    {"name": "Fanta", "cost": 23, "img": "./cola.jpg"}, 
    {"name": "Mirinda", "cost": 45, "img": "./cola.jpg"}, 
    {"name": "Red Bull", "cost": 45, "img": "./cola.jpg"}]

def all_goods():
    line = "<div class='container'>"

    for item in goods:
        line += f"<div><img src=\"{item['img']}\"> <h3>{item['name']}: {item['cost']} uhr.<h3><button>Buy</button></div>"

    line += "</div>\n"
    return line

with open('index.html', "w") as f:
    f.writelines(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./styles.css">
</head>
<body>
    <h1>Online shop</h1> """ + 
    all_goods()
    +
    """
</body>
</html>
    """)
