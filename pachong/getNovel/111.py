from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.innodealing.com/auth-service/signin")
    page.get_by_placeholder("DM账号/手机号").click()
    page.get_by_placeholder("DM账号/手机号").fill("18811087679")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("zhangxuji000")
    page.get_by_label("我已阅读并同意相关服务条款和政策").check()
    page.get_by_role("button", name="登录").click()
    page.frame_locator("iframe >> nth=0").locator(".nY5g3oU45oPl4aioSr5\\+ag\\=\\=").click()
    page.frame_locator("iframe >> nth=0").get_by_text("首页").first.click()
    page.frame_locator("iframe >> nth=0").get_by_role("button", name="历史成交").click()
    page.frame_locator("iframe >> nth=0").locator("div").filter(has_text="万科企业股份有限公司").nth(1).click()
    # page.frame_locator("iframe >> nth=0").get_by_role("combobox").filter(has_text="万科企业股份有限公司").nth(1).click()
    page.frame_locator("iframe >> nth=0").get_by_role("combobox").filter(has_text="万科企业股份有限公司").get_by_role("textbox").fill("驻马店市产业投资集团有限公司")
    page.frame_locator("iframe >> nth=0").get_by_role("menuitem", name="驻马店市产业投资集团有限公司", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
