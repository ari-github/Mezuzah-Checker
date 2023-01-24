from diff_match_patch import diff_match_patch

mez_letters = "שמע ישראל יהוה אלהינו יהוה אחד ואהבת את יהוה אלהיך בכל לבבך ובכל נפשך ובכל מאדך והיו הדברים האלה אשר אנכי מצוך היום על לבבך ושננתם לבניך ודברת בם בשבתך בביתך ובלכתך בדרך ובשכבך ובקומך וקשרתם לאות על ידך והיו לטטפת בין עיניך וכתבתם על מזזות ביתך ובשעריך והיה אם שמע תשמעו אל מצותי אשר אנכי מצוה אתכם היום לאהבה את יהוה אלהיכם ולעבדו בכל לבבכם ובכל נפשכם ונתתי מטר ארצכם בעתו יורה ומלקוש ואספת דגנך ותירשך ויצהרך ונתתי עשב בשדך לבהמתך ואכלת ושבעת השמרו לכם פן יפתה לבבכם וסרתם ועבדתם אלהים אחרים והשתחויתם להם וחרה אף יהוה בכם ועצר את השמים ולא יהיה מטר והאדמה לא תתן את יבולה ואבדתם מהרה מעל הארץ הטבה אשר יהוה נתן לכם ושמתם את דברי אלה על לבבכם ועל נפשכם וקשרתם אתם לאות על ידכם והיו לטוטפת בין עיניכם ולמדתם אתם את בניכם לדבר בם בשבתך בביתך ובלכתך בדרך ובשכבך ובקומך וכתבתם על מזוזות ביתך ובשעריך למען ירבו ימיכם וימי בניכם על האדמה אשר נשבע יהוה לאבתיכם לתת להם כימי השמים על הארץ"
num_to_let = {1: 'א', 2: 'ב', 3: 'ג', 4: 'ד', 5: 'ה', 6: 'ו', 7: 'ז', 8: 'ח', 9: 'ט', 10: 'י', 20: 'כ', 30: 'ל',
              40: 'מ', 50: 'נ', 60: 'ס', 70: 'ע', 80: 'פ', 90: 'צ', 100: 'ק', 200: 'ר', 300: 'ש', 400: 'ת',
              21: 'ך', 41: 'ם', 51: 'ן', 81: 'ף', 91: 'ץ'}


def find_difference(test_letters):
    dmp = diff_match_patch()
    diff = dmp.diff_main(test_letters, mez_letters)
    # ignore whitespaces
    for i, d in enumerate(diff):
        if d[0] != 0 and d[1] == " ":
            diff[i] = (0, diff[i][1])

    # print(diff)
    # print(dmp.diff_prettyHtml(diff))

    return diff


def get_error_list(diff):
    errors = []
    counter = 0
    for i, d in enumerate(diff):
        if d[0] == 0:
            counter += len(d[1].replace(" ", ""))
        elif d[0] == -1:
            bed = d[1].replace(" ", "")
            errors.append({"error": "-", "index": counter, "old": bed})
            counter += len(bed)
        elif d[0] == 1:
            last_err = errors[-1] if errors else None
            if last_err and last_err["error"] == "-" and last_err["index"] + len(last_err["old"]) >= counter:
                last_err["error"] = "!"
                last_err["new"] = d[1]
            else:
                errors.append({"error": "+", "index": counter, "new": d[1]})

    return errors


def go_over_results(errors, letter_list, img):
    for e in errors:
        if e['error'] == "!":
            print(f"Detected as: {e['old']} need to be: {e['new']}")
            letter_list[e["index"]].show_let(img.copy())
        elif e['error'] == "-":
            print(f"Detected as: {e['old']} need to be delete")
            letter_list[e["index"]].show_let(img.copy())
        elif e['error'] == '+':
            print(f"Need to add: {e['new']}")
            letter_list[e["index"]].show_let(img.copy())


def get_matching(letter_list, img):
    test_letters = "".join(num_to_let[let.prediction] for let in letter_list)

    diff = find_difference(test_letters)

    errors = get_error_list(diff)

    go_over_results(errors, letter_list, img)
    # print(errors)

    return errors
