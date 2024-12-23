import asyncio
from playwright.async_api import async_playwright


async def parse_twitch():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Запуск браузера в режиме с отображением окна
        page = await browser.new_page()

        # Открытие страницы Twitch
        await page.goto('https://www.twitch.tv')

        search_box = page.locator('input[autocomplete="twitch-nav-search"]')
        await search_box.type("Music")

        # Ждем появления результата поиска
        await page.wait_for_selector('div.Layout-sc-1xcs6mc-0.auOiD')

        # Кликаем на результат с тегами
        await page.locator('div#search-result-row__0').click()

        # Ожидание полной загрузки страницы
        await page.wait_for_load_state('networkidle')

        # Пример: получение названий топовых игр
        try:
            await page.wait_for_selector("div.Layout-sc-1xcs6mc-0.dUClxi", timeout=20000)
            top_games_locator = page.locator("div.ScTower-sc-1sjzzes-0.fwymPs.tw-tower")
            top_games_locator = top_games_locator.locator("div.Layout-sc-1xcs6mc-0.dUClxi")
            if await top_games_locator.count() > 0:
                for i in range(await top_games_locator.count()):
                    game_locator = top_games_locator.nth(i)
                    title = await game_locator.locator("h3.CoreText-sc-1txzju1-0.MveHm").inner_text() or "Неизвестно"

                    # Имя стримера
                    streamer = await game_locator.locator("p[data-a-target='preview-card-channel-link']").inner_text() or "Неизвестно"

                    # Количество зрителей
                    viewers = await game_locator.locator(".ScMediaCardStatWrapper-sc-anph5i-0").inner_text() or "Неизвестно"

                    # Тэги
                    tag_placers = game_locator.locator(".InjectLayout-sc-1i43xsx-0.gNgtQs")
                    tag_elements = tag_placers.locator(".InjectLayout-sc-1i43xsx-0")  # Находим все подходящие элементы
                    tags = []
                    if await tag_elements.count() > 0:
                        for k in range(await tag_elements.count()):
                            tag = await tag_elements.nth(k).inner_text()
                            tags.append(tag)  # Собираем текст всех элементов
                    tags_text = ", ".join(tags) if tags else "Неизвестно"

                    print(
                        f"Заголовок: {title}\n   Стример: {streamer}\n   Зрителей: {viewers}\n   Тэги: {tags_text}")
            else:
                print("Топовые игры не найдены.")
        except Exception as e:
            print(f"Ошибка при загрузке топовых игр: {e}")

        await browser.close()


# Запуск асинхронной функции
asyncio.run(parse_twitch())