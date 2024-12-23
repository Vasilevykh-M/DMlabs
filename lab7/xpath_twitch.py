import asyncio
from playwright.async_api import async_playwright

async def parse_twitch():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Запуск браузера в режиме с отображением окна
        page = await browser.new_page()

        # Открытие страницы Twitch
        await page.goto('https://www.twitch.tv')

        # Ожидание полной загрузки страницы
        await page.wait_for_load_state('networkidle')

        # Пример: получение названий топовых игр
        try:
            await page.wait_for_selector("//div[contains(@class, 'ScTower-sc-1sjzzes-0') and contains(@class, 'fwymPs') and contains(@class, 'tw-tower')]", timeout=20000)
            top_games_locator = page.locator("//div[contains(@class, 'ScTower-sc-1sjzzes-0') and contains(@class, 'fwymPs') and contains(@class, 'tw-tower')]")
            top_games_locator = top_games_locator.locator("//div[contains(@class, 'OBUFH') and contains(@class, 'ScTransitionBase-sc-hx4quq-0') and contains(@class, 'tw-transition')]")

            if await top_games_locator.count() > 0:
                for i in range(await top_games_locator.count()):
                    game_locator = top_games_locator.nth(i)
                    title = await game_locator.locator("//button[@data-test-selector='StreamTitle']//h3").inner_text() or "Неизвестно"

                    # Имя стримера
                    streamer = await game_locator.locator("//p[@data-a-target='preview-card-channel-link']").inner_text() or "Неизвестно"

                    # Количество зрителей
                    viewers = await game_locator.locator("//div[contains(@class, 'ScMediaCardStatWrapper-sc-anph5i-0')]").inner_text() or "Неизвестно"

                    # Тэги
                    tag_placers = game_locator.locator("//div[contains(@class, 'InjectLayout-sc-1i43xsx-0') and contains(@class, 'gNgtQs')]")
                    tag_elements = tag_placers.locator("//div[contains(@class, 'InjectLayout-sc-1i43xsx-0')]")
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