from selenium.webdriver.common.by import By


class DynamicPropertiesLocators(object):
    ELEMENTS_PROP_CARD = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[1]")
    DYNAMIC_PROP_SECTION = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[1]/div/ul[@class='menu-list']/li[9]/span[@class='text']")
    RANDOM_TEXT_ID = (By.XPATH, "//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']//p[.='This text has random Id']")
    VISIBLE_AFTER = (By.ID, "visibleAfter")
    ENABLE_BUTTON = (By.ID, "enableAfter")
    COLOR_CHANGE = (By.ID, "colorChange")

class DragAndDropLocators(object):

    INTERACTIONS_PAGE = (By.XPATH,"//div[@id='app']/div[@class='body-height']/div[@class='home-content']//div[@class='category-cards']/div[5]/div")
    DROPPABLE_PAGE = (By.XPATH,"//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[5]/div/ul[@class='menu-list']/li[4]/span[@class='text']")
    DRAGGABLE_BOX = (By.CSS_SELECTOR,"div#draggable")
    DROPPABLE_BOX = (By.CSS_SELECTOR,"#simpleDropContainer #droppable")

class HoverElementsLocators(object):

    WIDGETS_PROP_CARD = (By.XPATH,"//div[@id='app']/div[@class='body-height']/div[@class='home-content']/div[@class='home-body']/div/div[4]/div/div[@class='card-body']")
    TOOL_TIP = (By.XPATH,"//div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']//div[@class='accordion']/div[4]/div/ul[@class='menu-list']/li[7]")
