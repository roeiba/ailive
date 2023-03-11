from ailive.actions.plugins.readers.bbc_titles_reader import AliveBBCNewsPlugin
from ailive.actions.plugins.writers.wordpress import WordPressAlivePlugin
from ailive.config import settings
from ailive.engine.chatgpt.prompts.news_prompts import summarization_prompt
from ailive.infra import log_config  # noqa: F401
from ailive.infra.base_entity import AiLive


class NewsSummarizer(AiLive):
    def get_plugins(self):
        plugins = []
        wp_config = settings.plugins.wordpress1
        wordpress_plugin = WordPressAlivePlugin(
            base_url=wp_config.base_url,
            username=wp_config.username,
            password=wp_config.password,
        )
        plugins.append(wordpress_plugin)
        news_plugin = AliveBBCNewsPlugin()
        plugins.append(news_plugin)
        return plugins


def main():
    alive_bot = NewsSummarizer(
        prompt=summarization_prompt,
        sleep_seconds=60)
    alive_bot.run_forever()


if __name__ == '__main__':
    main()
