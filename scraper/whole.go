// whole.go
// capture full-page screenshots of each lesson page into the images/ directory.
package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/playwright-community/playwright-go"
)

// clean converts a lesson title into a safe file name.
func clean(s string) string {
	r := strings.NewReplacer(" ", "_", ":", "", "/", "_")
	return strings.ToLower(r.Replace(s))
}

func main() {
	pw, err := playwright.Run()
	if err != nil {
		log.Fatalf("playwright: %v", err)
	}
	defer pw.Stop()

	browser, err := pw.Chromium.Launch(playwright.BrowserTypeLaunchOptions{
		Headless: playwright.Bool(true),
	})
	if err != nil {
		log.Fatalf("browser: %v", err)
	}
	defer browser.Close()

	page, err := browser.NewPage()
	if err != nil {
		log.Fatalf("page: %v", err)
	}

	// login
	page.Goto("https://python.cs.muzoo.io/protected/lessons/01/welcome/")
	page.Fill("#username", "u6781617")
	page.Fill("#password", "REMOVE")
	page.Check("#rememberMe")
	page.Click("#kc-login")
	page.WaitForLoadState()

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

	os.MkdirAll("images", 0755)

	for title, url := range lessons {
		fmt.Println(title)
		if _, err := page.Goto(url); err != nil {
			log.Printf("skip %s: %v", url, err)
			continue
		}

		boxes, _ := page.QuerySelectorAll(".muzoo-problembox")
		for _, b := range boxes {
			b.ScrollIntoViewIfNeeded()
			page.WaitForTimeout(200)
			if l, _ := b.QuerySelector(".CodeMirror-line"); l != nil {
				l.Click()
				page.WaitForTimeout(100)
			}
		}
		page.WaitForTimeout(500)

		_, err = page.Screenshot(playwright.PageScreenshotOptions{
			Path:     playwright.String(fmt.Sprintf("images/%s.png", clean(title))),
			FullPage: playwright.Bool(true),
		})
		if err != nil {
			log.Printf("screenshot %s: %v", title, err)
		}
	}
	fmt.Println("done")
}
