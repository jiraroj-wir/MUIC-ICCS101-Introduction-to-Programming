// exercise_box.go
// capture each exercise box individually; screenshots are grouped in images/<lesson>/boxXX.png
package main

import (
	"fmt"
	"log"
	"os"
	"strings"

	"github.com/playwright-community/playwright-go"
)

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

	// login once
	page.Goto("https://python.cs.muzoo.io/protected/lessons/01/welcome/")
	page.Fill("#username", "u6781617")
	page.Fill("#password", "REMOVE")
	page.Check("#rememberMe")
	page.Click("#kc-login")
	page.WaitForLoadState()

	lessons := []struct{ title, url string }{
		{"Getting Started With Python", "https://python.cs.muzoo.io/protected/lessons/02/getting-started/"},
		{"Further Expressions", "https://python.cs.muzoo.io/protected/lessons/03/further-expressions/"},
		{"Type annotation and Strings", "https://python.cs.muzoo.io/protected/lessons/04/type-annotation-and-strings/"},
		{"Functions", "https://python.cs.muzoo.io/protected/lessons/05/functions/"},
		{"Making Decisions", "https://python.cs.muzoo.io/protected/lessons/06/conditional/"},
		{"Lists and The For Loop", "https://python.cs.muzoo.io/protected/lessons/07/lists-and-for/"},
		{"Unit testing and while loop", "https://python.cs.muzoo.io/protected/lessons/08/asserts-and-while/"},
		{"Learn by Examples I", "https://python.cs.muzoo.io/protected/lessons/09/learn-by-examples-i/"},
		{"Learn by Examples II", "https://python.cs.muzoo.io/protected/lessons/10/learn-by-examples-ii/"},
		{"Tuples and Nested Structures", "https://python.cs.muzoo.io/protected/lessons/13/tuple-nested/"},
		{"References", "https://python.cs.muzoo.io/protected/lessons/14/references/"},
		{"Sets", "https://python.cs.muzoo.io/protected/lessons/15/sets/"},
		{"Dictionaries", "https://python.cs.muzoo.io/protected/lessons/16/dictionaries/"},
		{"Recursion", "https://python.cs.muzoo.io/protected/lessons/17/recursion/"},
		{"Recursion II", "https://python.cs.muzoo.io/protected/lessons/18/recursion-ii/"},
		{"Working with Text Files", "https://python.cs.muzoo.io/protected/lessons/19/files/"},
		{"Exception Handling", "https://python.cs.muzoo.io/protected/lessons/20/exceptions/"},
		{"Classes & Objects I", "https://python.cs.muzoo.io/protected/lessons/21/objects-i/"},
		{"Classes & Objects II", "https://python.cs.muzoo.io/protected/lessons/22/objects-ii/"},
		{"For/List Comprehension", "https://python.cs.muzoo.io/protected/lessons/23/comprehension/"},
		{"Game Development with OOP (Optional)", "https://python.cs.muzoo.io/protected/lessons/23X/game/"},
	}

	for _, les := range lessons {
		fmt.Println(les.title)
		if _, err := page.Goto(les.url); err != nil {
			log.Printf("skip %s: %v", les.url, err)
			continue
		}

		dir := fmt.Sprintf("images/%s", clean(les.title))
		os.MkdirAll(dir, 0755)

		boxes, _ := page.QuerySelectorAll(".muzoo-problembox")
		for i, box := range boxes {
			box.ScrollIntoViewIfNeeded()
			page.WaitForTimeout(200)

			if cm, _ := box.QuerySelector(".CodeMirror-scroll"); cm != nil {
				cm.Evaluate(`el => el.scrollTo(0, el.scrollHeight)`)
				page.WaitForTimeout(100)
			}

			fname := fmt.Sprintf("%s/box%02d.png", dir, i+1)
			if _, err := box.Screenshot(playwright.ElementHandleScreenshotOptions{
				Path: playwright.String(fname),
			}); err != nil {
				log.Printf("screenshot error: %v", err)
			}
		}
	}
	fmt.Println("done")
}
