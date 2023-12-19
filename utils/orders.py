from loader import db


async def order_to_text(order):
    """Convert order object to readable text"""
    res = ""
    product_id, count = order[3].split("=")
    product = db.fetchone("SELECT * FROM products WHERE idx=?", (product_id,))
    res += f"Заказ <b>№{order[3]}</b>\n\n"
    res += f"Товар: <b>{product[1]}</b>\n"
    res += f"Количество: <b>{count}</b>\n"
    res += f"Цена: <b>{product[4]}</b>\n"
    res += f"Имя: <b>{order[1]}</b>\n"
    res += f"Адрес: <b>{order[2]}</b>\n"
    return res
