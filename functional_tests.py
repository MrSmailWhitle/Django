from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewvisitorTest(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
	def tearDown(self):
		self.driver.quit()
	def test_found_todo(self):	
		self.driver.get('http://localhost:8000')
		time.sleep(2)
#公司新增了一个代办事项管理工具
#白去首页查看，标题和头部有to-do的提示
		self.assertIn( 'To-Do',self.driver.title)
		headtext=self.driver.find_element_by_tag_name('h1').text
		self.assertIn('To-Do',headtext)
#他输入了第一个代办事项，test hoden
		input=self.driver.find_element_by_id("id_new_item");
		self.assertEqual(input.get_attribute('placeholder'),"Enter a to-do item")
		input.send_keys('test hoden')
#完成输入后，enter页面刷新了
		input.send_keys(Keys.ENTER)
		time.sleep(1)
#这时页面出现了一条代办事项；1. test hoden；
		table=self.driver.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text=='1.test hoden' for row in rows),"new to do item not appear in table")
#页面此时又刷新了一个新的输入框，可以输入新的代办事项
#白输入了代办事项：2.retry bugs
#完成输入后，页面刷新了输入框；同时出现了代办事项列表更新为2个
#白确定可以记录个人的唯一url
#白重新打开这个网站，代办信息还在
		
		self.fail('Finish the test!')
if __name__=='__main__':
	unittest.main(warnings='ignore')