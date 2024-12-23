import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def parse_twitch():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Запуск браузера в режиме с отображением окна
        page = await browser.new_page()

        # Открытие страницы Twitch
        await page.goto('https://www.twitch.tv')

        # Ожидание полной загрузки страницы
        await page.wait_for_load_state('networkidle')

        # Получение HTML-кода страницы
        html_content = await page.content()

        # Закрытие браузера
        await browser.close()

    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Пример: получение названий топовых игр
    try:
        top_games = soup.select("div.ScTower-sc-1sjzzes-0.fwymPs.tw-tower div.OBUFH.ScTransitionBase-sc-hx4quq-0.tw-transition")
        if top_games:
            for game in top_games:
                title = game.select_one("button[data-test-selector='StreamTitle'] h3").get_text(strip=True) if game.select_one("button[data-test-selector='StreamTitle'] h3") else "Неизвестно"

                # Имя стримера
                streamer = game.select_one("p[data-a-target='preview-card-channel-link']").get_text(strip=True) if game.select_one("p[data-a-target='preview-card-channel-link']") else "Неизвестно"

                # Количество зрителей
                viewers = game.select_one(".ScMediaCardStatWrapper-sc-anph5i-0").get_text(strip=True) if game.select_one(".ScMediaCardStatWrapper-sc-anph5i-0") else "Неизвестно"

                # Тэги
                tag_elements = game.select(".InjectLayout-sc-1i43xsx-0.gNgtQs .InjectLayout-sc-1i43xsx-0")
                tags = [tag.get_text(strip=True) for tag in tag_elements]
                tags_text = ", ".join(tags) if tags else "Неизвестно"

                print(
                    f"Заголовок: {title}\n   Стример: {streamer}\n   Зрителей: {viewers}\n   Тэги: {tags_text}")
        else:
            print("Топовые игры не найдены.")
    except Exception as e:
        print(f"Ошибка при загрузке топовых игр: {e}")

# Запуск асинхронной функции
asyncio.run(parse_twitch())