import asyncio
from ui.dashboard import PromptMachineApp

async def main():
    app = PromptMachineApp()
    async with app.run_test(size=(120, 35)) as pilot:
        await pilot.pause(1)
        app.save_screenshot("tui-screenshot.svg")
        print("Screenshot saved to tui-screenshot.svg")

if __name__ == "__main__":
    asyncio.run(main())
