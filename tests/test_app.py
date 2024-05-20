from playwright.sync_api import Page, expect

def test_log_in_successful(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Log in")
    page.fill("input[name='email']", "charliegiaretta@outlook.com")
    page.fill("input[name='password']", "password123")
    page.click('text="Log in"')
    logged_in_tag = page.locator(".t-login-message")
    expect(logged_in_tag).to_have_text("Logged in as: charliegiaretta")

def test_post_peep(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Log in")
    page.fill("input[name='email']", "charliegiaretta@outlook.com")
    page.fill("input[name='password']", "password123")
    page.click('text="Log in"')
    page.fill("textarea[name='content']", "test content")
    page.click('text="Post a peep"')
    content_tag = page.locator(".t-content")
    expect(content_tag).to_have_text("test content")

def test_register_with_valid_credentials(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.click("text=Sign up")
    page.fill("input[name='username']", "testuser")
    page.fill("input[name='email']", "testuser@email.com")
    page.fill("input[name='password']", "testuser")
    page.click("text=Sign up")
    p_tag = page.locator("p")
    expect(p_tag).to_have_text("Account creation successful")
    page.click("text=Log in")
    page.fill("input[name='email']", "testuser@email.com")
    page.fill("input[name='password']", "testuser")
    page.click('text="Log in"')
    logged_in_tag = page.locator(".t-login-message")
    expect(logged_in_tag).to_have_text("Logged in as: testuser")
