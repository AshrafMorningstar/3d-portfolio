from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Capture console messages
    page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
    page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))

    try:
        print("Navigating to http://localhost:8000/index.html")
        page.goto("http://localhost:8000/index.html")

        # Wait for potential initial animations or loading
        time.sleep(2)

        print("Taking initial screenshot...")
        page.screenshot(path="tests/initial.png")

        # Check for key elements (the HUD)
        if page.locator(".hud").is_visible():
            print("HUD is visible.")
        else:
            print("HUD is NOT visible.")

        # Simulate mouse movement
        print("Simulating mouse movement...")
        page.mouse.move(100, 100)
        time.sleep(0.5)
        page.mouse.move(500, 500)
        time.sleep(0.5)

        # Simulate click (Warp)
        print("Simulating click (Warp)...")
        page.mouse.down()
        time.sleep(1) # Hold for a bit to let the warp effect happen

        print("Taking warping screenshot...")
        page.screenshot(path="tests/warping.png")

        page.mouse.up()
        time.sleep(1)

    except Exception as e:
        print(f"ERROR: {e}")

    finally:
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
