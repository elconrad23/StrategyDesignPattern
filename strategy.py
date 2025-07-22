from abc import ABC, abstractmethod

# Syda Namugarura, Patience Agenorwot, Conrad Waako, Linda Peruth, Ejidia Uwabeza, Josephine Kulabako
# Observer interface: all observers must implement the update() method
class Observer(ABC):
    @abstractmethod
    def update(self, news):
        pass


# Subject interface: all subjects must implement these methods
class Subject(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Concrete Subject class
class NewsAgency(Subject):
    def __init__(self):
        # List to store all registered observers
        self._observers = []
        self._news = None

    def register(self, observer):
        # Add an observer
        self._observers.append(observer)

    def remove(self, observer):
        # Remove an observer
        self._observers.remove(observer)

    def publish_news(self, news):

        self._news = news
        self.notify_observers()

    def notify_observers(self):
        # Call update() on all registered observers
        for observer in self._observers:
            observer.update(self._news)


# Concrete Observer classes
class PhoneSubscriber(Observer):
    def update(self, news):
        print(f"[PhoneSubscriber] News updated: {news}")
        
        
class EmailSubscriber(Observer):
    def update(self, news):
        print(f"[EmailSubscriber] News updated: {news}")

    # Create subject
if __name__ == "__main__":
    news_agency = NewsAgency()

    # Create observers
    phone_subscriber = PhoneSubscriber()
    email_subscriber = EmailSubscriber()

    # Register observers
    news_agency.register(phone_subscriber)
    # news_agency.register(email_subscriber)

    # # Publish news - all observers are notified
    news_agency.publish_news("Breaking News: New Observer Pattern Tutorial Released!")

    # # Remove email subscriber
    # news_agency.remove(email_subscriber)

    # # Publish news again - only phone subscriber is notified
    news_agency.publish_news("Update: Observer pattern example refined!")