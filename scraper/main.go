package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/playwright-community/playwright-go"
)

func cleanFileName(name string) string {
	name = strings.ReplaceAll(name, " ", "_")
	name = strings.ReplaceAll(name, ":", "")
	name = strings.ReplaceAll(name, "/", "_")
	return strings.ToLower(name)
}

func main() {
	pw, err := playwright.Run()
	if err != nil {
		log.Fatalf("could not launch playwright: %v", err)
	}
	browser, err := pw.Chromium.Launch(playwright.BrowserTypeLaunchOptions{
		Headless: playwright.Bool(true),
	})
	if err != nil {
		log.Fatalf("could not launch browser: %v", err)
	}
	page, err := browser.NewPage()
	if err != nil {
		log.Fatalf("could not create page: %v", err)
	}

	// login
	_, err = page.Goto("https://python.cs.muzoo.io/protected/lessons/01/welcome/")
	if err != nil {
		log.Fatalf("could not go to login page: %v", err)
	}

	page.Fill("#username", "u6781617")
	page.Fill("#password", "REMOVED")
	page.Check("#rememberMe")

	err = page.Click("#kc-login", playwright.PageClickOptions{
		Timeout: playwright.Float(3000),
	})
	if err != nil {
		log.Fatalf("login click failed: %v", err)
	}

	lessons := map[string]string{
		"Getting Started With Python":          "https://python.cs.muzoo.io/protected/lessons/02/getting-started/",
		"Further Expressions":                  "https://python.cs.muzoo.io/protected/lessons/03/further-expressions/",
		"Type annotation and Strings":          "https://python.cs.muzoo.io/protected/lessons/04/type-annotation-and-strings/",
		"Functions":                            "https://python.cs.muzoo.io/protected/lessons/05/functions/",
		"Making Decisions":                     "https://python.cs.muzoo.io/protected/lessons/06/conditional/",
		"Lists and The For Loop":               "https://python.cs.muzoo.io/protected/lessons/07/lists-and-for/",
		"Unit testing and while loop":          "https://python.cs.muzoo.io/protected/lessons/08/asserts-and-while/",
		"Learn by Examples I":                  "https://python.cs.muzoo.io/protected/lessons/09/learn-by-examples-i/",
		"Learn by Examples II":                 "https://python.cs.muzoo.io/protected/lessons/10/learn-by-examples-ii/",
		"Tuples and Nested Structures":         "https://python.cs.muzoo.io/protected/lessons/13/tuple-nested/",
		"References":                           "https://python.cs.muzoo.io/protected/lessons/14/references/",
		"Sets":                                 "https://python.cs.muzoo.io/protected/lessons/15/sets/",
		"Dictionaries":                         "https://python.cs.muzoo.io/protected/lessons/16/dictionaries/",
		"Recursion":                            "https://python.cs.muzoo.io/protected/lessons/17/recursion/",
		"Recursion II":                         "https://python.cs.muzoo.io/protected/lessons/18/recursion-ii/",
		"Working with Text Files":              "https://python.cs.muzoo.io/protected/lessons/19/files/",
		"Exception Handling":                   "https://python.cs.muzoo.io/protected/lessons/20/exceptions/",
		"Classes & Objects I":                  "https://python.cs.muzoo.io/protected/lessons/21/objects-i/",
		"Classes & Objects II":                 "https://python.cs.muzoo.io/protected/lessons/22/objects-ii/",
		"For/List Comprehension":               "https://python.cs.muzoo.io/protected/lessons/23/comprehension/",
		"Game Development with OOP (Optional)": "https://python.cs.muzoo.io/protected/lessons/23X/game/",
	}

	os.MkdirAll("test", os.ModePerm)

	for title, url := range lessons {
		log.Println("visiting:", url)
		_, err := page.Goto(url)
		if err != nil {
			log.Printf("failed to access %s: %v", url, err)
			continue
		}

		// prevent lazy loading, or what ever makes the embeded exercises unshown
		page.EvalOnSelectorAll(".muzoo-problembox", "(els) => els.forEach(el => el.scrollIntoView({block: 'center'}))")

		page.WaitForSelector(".CodeMirror-line", playwright.PageWaitForSelectorOptions{
			Timeout: playwright.Float(2000),
		})

		filename := fmt.Sprintf("test/%s.png", cleanFileName(title))
		_, err = page.Screenshot(playwright.PageScreenshotOptions{
			Path:     playwright.String(filename),
			FullPage: playwright.Bool(true),
		})
		if err != nil {
			log.Printf("screenshot failed for %s: %v", title, err)
			continue
		}
	}

	browser.Close()
	pw.Stop()
}
