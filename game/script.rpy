﻿define pc = Character("Комп’ютер")
define form = Character("Форма")

define girl = Character("Дівчина")
define boy = Character("Хлопець")
define boy1 = Character("Хлопець 1")
define boy2 = Character("Хлопець 2")
define stud1 = Character("Студент 1")
define stud2 = Character("Студентка 2")
define stud3 = Character("Студент 3")

define main = Character("Ви")
define cpp = Character("Сі")
define ruby = Character("Рубі")
define py = Character("Пай")
define thon = Character("Тон")
define java = Character("Джава")
define js = Character("Ярик")


label start:
    scene bg pc

    pc "Вам надійшов лист: \"Добрий день, шановний абітурієнт. Раді повідомити Вам, що по результатам конкурсу Ви пройшли на бюджет до найкращого університету ЧНУ ім. П. Могили!..."
    pc "... Щоб продовжити процедуру вступу, пройдіть, будь ласка, за посиланням для детальної інформації щодо необхідних документів та часів роботи приймальної комісії.\""

    menu:
        "Прийняти запрошення на вступ?"

        "Так":
            "Ви переходите за посиланням. Після вивчення усієї інформації на сторінці, Ви переходити на форму для онлайн-запису до приймальної комісії."

            python:
                main_name = renpy.input("Ваше ім'я:")

            menu:
                form "Ваша стать:"

                "Жінка":
                    python:
                        main_gender = 0

                "Чоловік":
                    python:
                        main_gender = 1

                "Не вказано":
                    python:
                        main_gender = 2

            "Після заповнення ще деякої інформації..."

            form "Дякуємо, [main_name], що вирішили вступити до найкращого університету ЧНУ ім. П. Могили! З нетерпінням чекаємо Вас в наших стінах."

            jump intro_cpp

        "Ні":
            #TODO 1: bad ending :(
            
            return


label intro_cpp:
    scene black

    "Під кінець спекотного літа університет, в який Ви успішно поступили, проводить збір майбутніх студентів для ознайомлення з новим навчальним закладом та одногрупниками."
    "Вставши після дзвінка будильника, Ви збираєтесь на зустріч новим подіям та знайомствам."

    pause 2

    scene black #TODO 2: add bg "Фон: головний вхід до університету"

    "І ось Ви тут знову. Ви відчуваєте піднесення і деякий страх перед новою сторінкою Вашого життя. Скоро цей новий вхід до будівлі університету стане для Вас буденним."

    "Прямо перед Вашими очима стоїть стенд, на якому ще до початку навчального року вже висять об’яви. Ви зацікавлено підхидите."

    "Брошури для абітурієнтів, запрошення на курси англійської мови, телефони психологічної підтримки…"

    "Вас зацікавив плакат, на якому Ви бачите сьогоднішню дату. Великими буквами написано “Благодійний ярмарок”."

    if main_gender == 0:
        girl "Зацікавилась сьогоднішнім ярмарком?"
    elif main_gender == 1:
        girl "Зацікавився сьогоднішнім ярмарком?"
    elif main_gender == 2:
        girl "Зацікавились сьогоднішнім ярмарком?"
    
    "Несподівано Ви почули голос біля Вас. Повернувшись у напрямку, звідки він був, Ви побачили миловидну дівчину."

    show cpp happy

    girl "В навчальні дні у студентів не так багато часу читати якісь плакати на вході, тому вирішили почати ярмарок саме сьогодні."

    if main_gender == 0:
        girl "Ти ж першокурсниця, так?"
    elif main_gender == 1 or main_gender == 2:
        girl "Ти ж першокурсник, так?"

    "Ви киваєте головою, дивлячись на дівчину зі здивуванням."

    cpp "Вибач, зовсім забула представитись. Мене звуть Сі. Навчаюсь на другому курсі."

    main "Мене [main_name]. Приємно познайомитись…"

    cpp "На ярмарку ми продаємо різні поробки, зроблені дітками з дитячого будинку. Всі кошти підуть на купівлю нової одежі та іграшок для них."
    cpp "Ти дуже допоможеш, якщо щось купиш."
    cpp "Чи не хочеш подивитись на поробки? Тут не далеко, пару кроків і ось за тими дверима стоять стенди."

    "Схоже, Сі і правда дуже горить цим ділом, адже так швидко говорити ще й не запинатись не кожен репер може."

    menu: 
        "Піти з Сі?"

        "Так":
            main "В мене ще є час, тому чому б ні. Ось ті двері?"

            cpp "Так-так, пішли, я тебе проведу. Ти точно не пожалкуєш."
        
        "Ні":
            main "Вибач, але я не дуже зацікавлений в такого роду подіях."
            
            show cpp sad

            cpp "А-але так ти зможеш допомогти діткам.. Давай ти хоча б подивишся, м-можеш нічого не купувати."

    hide cpp happy

    "Ви разом з Сі заходите до кабінету, в якому на столах розставлені різні дитячі поробки. Янголятка, ляльки-мотанки, дома з картону та.."
    "Новорічна ялинка з паперу."
    "Ви точно не очікували побачити в кінці літа щось зимове, але це підняло Вам настрій." 
    "Ви вирішили купити як сувенір цю маленьку поробку, яка не вписувалась в навколишні обстановку, але тим і привернула Вашу увагу."

    show cpp happy

    cpp "Хіхі"
    cpp "А ой, вибач, я не з тебе сміялася."
    cpp "Просто не думала, що хтось в кінці літа вирішить її купити."
    cpp "Дякую тобі велике! Скоро почнеться посвята, тому не буду більше тебе затримувати. Бережи себе!"

    "Ви навіть не помітили, як швидко минув час за розгляданням поробок. Попрощавшись, Ви, дотримуючись вказівників, піднімаєтесь по сходам та заходите в актову залу."

    scene bg hall # TODO 3: find a new one (with people)

    "Здається, Ви встигнули. На перших сидіннях кожного ряду написано номер групи. Знайшовши свій, Ви просуваєтесь далі по ряду і сідаєте біля Ваших нових одногрупників."
    "Не довго чекаючи, на сцену вийшла дівчина і всі затихли. Так почалась посвята у студенти. Вас привітали зі вступом до університету, розповіли про традиції та щорічні заходи."
    "Вас познайомили з керуючими органами Вашого факультету, представили кураторів усіх груп, в тому числі і Вашої. Ви взнали про навчальну платформу, на якій Ви будете вчитися,..."
    "... розклад на семестр, як проходитиме сесія і всі інші початкові знання, необхідні першокурсникам."
    "В кінці декан провела мотиваційний виступ і посвятила Вас в студенти університету."
    "Після оплесків, всі почали швидко виходити з актової зали, тому Ви слідуєте за натовпом в сторону виходу."

    jump intro_ruby


label intro_ruby:
    scene bg corridor

    "Як виявляється, просторий коридор стає дуже маленьким, коли в ньому знаходяться багато людей. В метушні в втрачаєте з виду свого куратора та тих небагатьох одногрупників, з якими Ви сиділи поруч."
    "Після того, як більшість людей пішли разом зі своїми групами, Ви розгублено дивитесь по сторонам, шукаючи якісь вказівники."
    "Нічого не знайшовши, Ви вирішуєте знайти необхідний Вам напрямок дорослими методами. На еники-беники."

    main "А з якої краще сторони почати? Хай буде права. Еники-беники їли вареники…"

    girl "Хіхі"
    girl "Слухай, мені здається, це не найкращий спосіб вибору дороги."

    "Здавалось, вже в порожньому коридорі, до вас підійшла червоноволоса дівчина."

    show ruby happy

    ruby "Мене звуть Рубі. Я з 4 курсу, тому можу допомогти тобі знайти дорогу, якщо не хочеш блукати до ночі. Хіхі."

    main "[main_name]. Перший курс, група... Група… 109 наче. Так, 109."

    ruby "Ооо, то ти так довго блукати будеш. Ваш кабінет доволі далеченько. Хоча, зможеш познайомитися з усією будівлею за раз. Ну то що, провести?"

    menu: 
        "Піти з Рубі?"

        "Так":
            main "Так, будь ласка. Думаю, в мене ще цілий навчальний рік є для знайомства з тутешніми коридорами."

            ruby "Хіхі"
            ruby "І то правда."
            ruby "Щож, пішли."

            if main_gender == 0:
                ruby "Почала ти рахувати якраз з вірного напрямку."
            elif main_gender == 1:
                ruby "Почав ти рахувати якраз з вірного напрямку."
            elif main_gender == 2:
                ruby "Почали ти рахувати якраз з вірного напрямку."
        
        "Ні":
            main "Я думаю, що можу самостійно знайти. Але дякую, що запропонувала."
            
            show ruby normal

            ruby "Ну, в тебе ще цілий рік є для знайомства з тутешніми коридорами, тому можна сьогодні не починати своє дослідження"
            ruby "Не соромся, в мене є вільний час, тому провести тебе мені не складно."
        
    hide ruby normal

    "По дорозі до кабінету Ви скористалися можливістю і попитали Рубі щодо навчального процесу. Вона на все відповідала, навіть на, здавалось, дурні питання."
    "Рубі справила на Вас враження того старшокурсника, який все про все знає і готовий допомогти в будь-яку хвилину."
    "Дійшовши до необхідного кабінету, Рубі вказала на листок на дверях, де від руки було написано “109”."

    show ruby happy

    ruby "От ми й пришли."

    if main_gender == 0:
        ruby "Не думаю, що ти сильно запізнилася, тому можеш спокійно заходити."
    elif main_gender == 1:
        ruby "Не думаю, що ти сильно запізнився, тому можеш спокійно заходити."
    elif main_gender == 2:
        ruby "Не думаю, що ти сильно запізнилися, тому можеш спокійно заходити."
    
    main "Дякую. З тобою ми правда швидко дійшли."

    if main_gender == 0:
        main "Тоді, я пішла. Бувай."
    elif main_gender == 1:
        main "Тоді, я пішов. Бувай."
    elif main_gender == 2:
        main "Тоді, я пішли. Бувай."

    ruby "Була рада допомогти. Па-па."

    hide ruby happy

    "Провівши Рубі поглядом, Ви робите глибокий вдих і видих. Стукаєте в двері і відчиняєте."
    
    scene black
    pause 1
    scene bg class

    "Ви бачите свого куратора. Привітавшись, Ви проходите до аудиторії і сідаєте за вільну парту."
    "Куратор ще раз представляється. Судячи зі всього, Ви дійсно не сильно запізнились. Куратор починає проговорювати в деталях те, що Ви чули в актовій залі і те, про що розмовляли з Рубі."
    "Нова інформація була лише про Вашу групу. Ви бігло познайомились з одногрупниками, після чого куратор ще раз звернула Вашу увагу на розклад і відпустила Вас до першого навчального дня."

    scene black # TODO 4: find a bg

    "Разом з новими знайомими Ви виходите з будівлі, вирішивши ближче познайомитись у парку."

    scene bg park

    "Вам складно запам’ятати усіх одногруників, але Ви робите все можливе. З першого погляду Вам подобається новий колектив, тому Ви з задоволенням провели час в компанії."

    "Через кілька годин всі почали потихенько розходитись і Ви вирішили йти додому."
    "Попрощавшись зі всіма, Ви згадуєте усе, що сьогодні сталося і з нетерпінням чекаєте першого навчального дня."

    jump intro_python


label intro_python:
    scene bg pc

    "Сьогодні Ваш перший навчальний день. За розкладом, Ваша перша пара - лекція, яка починається о 10:30. Ви вже давно прокинулись і поснідали, тому не поспішаючи збираєтесь до університету."

    "Дорогою до будівлі Ви згадуєте, як гарно провели час з одногрупниками. Також пригадуєте Ваших нових знайомих: Сі та Рубі і з нетерпінням чекаєте зустрічі з новими цікавими людьми."

    scene black # TODO 5: add bg

    pause 1

    scene bg corridor

    pause 1

    scene bg class

    "Ви заходите до аудиторії. У всередині вже достатньо багато людей, хоча Ви прийшли доволі рано. Майже всі студенти розбилися або по марам, або по невеличким групкам і не звертають на Вас уваги."
    "Пройшовши всю аудиторію очима, Ви шукаєте місце щоб сісти."
    "Ваш погляд чіпляється за хлопця, який маше Вам, підзиваючи до себе. Біля нього є вільне місце. Через відсутність варіантів, Ви вирішуєте підійти."
    "Зробивши кілька кроків вперед, Ви помічаєте, що біля хлопця сидить дівчина з неймовірною схожістю у зовнішності зі своїм сусідом по парті. Але вираз обличчя зовсім не такий радісний, навіть роздратований."
    "Дівчина крадькома подивилась на Вас і тут же відвернулась."
    "Ви все таки підходите до парти."

    show thon happy at left
    show py angry at right

    boy "Привіт-привіт. Тут вже всі по групкам  розбились, а одному бути не так весело, тому сідай коло нас!"

    main "Ви точно не проти?"
    main "Обидва."

    boy "Звісно ні! Я ж сам тебе покликав, тому не хвилюйся і сідай скоріше."

    menu: 
        "Сісти з хлопцем?"

        "Так":
            main "Що ж, якщо все добре, тоді дякую."

            "Ви сідаєте поруч з хлопцем. Дівчина все ще виглядає роздратованою."
        
        "Ні":
            main "Дякую за пропозицію, але я краще ще місце пошукаю. Може підсяду до одногрупників."

            show thon sad at left

            boy "Ну чого ти так. Сам же бачив, що один сидіти будеш."

            girl "Сідай вже. Тебе стільки разів запрошують, не гарно знову відмовляти."

            "Ви сідаєте поруч з хлопцем. Ви крадькома побачили легку посмішку дівчини, але перетнувшись з нею поглядами, вона знову перейшла до роздратованого стану."
            
    show thon happy at left

    boy "Ааа, от чого ти хвилювався."

    boy "Все нормально, Пай просто ще не звикла до такої кількості нових людей. Насправді, вона теж рада, так?"

    py "Угу, типо того."

    thon "А мене Тон звуть. Будемо знайомі."

    main "[main_name]. Теж приємно познайомитись."

    thon "То з якої ти групи? Ми разом з Пай з 108."

    main "109. А Ви з Пай, часом, не родичі?"

    py "А ти як думаєш?"

    if main_gender == 0:
        main "Ну, ви досить схожі, окрім кольору волосся і очей. Але все таки вирішила спитати."
        main "То я права?"
    elif main_gender == 1:
        main "Ну, ви досить схожі, окрім кольору волосся і очей. Але все таки вирішив спитати."
        main "То я правий?"
    elif main_gender == 2:
        main "Ну, ви досить схожі, окрім кольору волосся і очей. Але все таки вирішили спитати."
        main "То я праві?"

    thon "Саме так! Складно повірити, але ми з Пай брат і сестра. Двійняшки, якщо бути точним."

    py "І я старша. Народилася на 2 хвилини раніше."

    thon "На цілих 2 хвилини!"

    py "Час - це лише цифри. Факт залишається фактом. І можу сказати, що, на мою думку, я досить вдало справляюсь з роллю старшої сестри."

    thon "Звісно-звісно. Особливо коли треба лаяти когось."

    thon "Ай!"

    show py happy

    "Пай щипнула Тона за руку. Здається, вони добре ладять. Ви хотіли ще щось запитати, але в цей момент авдиторія притихла - зайшов викладач."

    hide thon happy
    hide py happy

    "Перша лекція пройшла доволі успішно. Вам цікаво розказали про предмет, навіщо він потрібен і де використовуються знання з нього і базовий матеріал."
    "Єдине, Вам було важко сидіти цілих 80 хвилин, а от Пай і Тон, здавалось, звикли до такого."

    "Після закінчення лекції, всі хутко почали збирати речі і виходити з аудиторії. Ви, Пай і Тон, також почали збиратися."

    show py normal at left
    show thon normal at right

    thon "Куди це всі так поспішають? В нас наче зараз велика перерва, на пару не запізнитись."

    py "Тому і поспішають, що перерва велика, і можна в їдальні поїсти. Там же черга така, що за всі 40 хвилин можуть й не встигнути поїсти."

    main "Настільки велика черга?"

    py "Угу, тому і поспішають так. Нам це не треба, ми з собою їжу беремо, а дивлячись на твою сумку, тобі, напевно, теж треба поспішати."

    thon "І правда."

    thon "Знаєш де їдальня знаходиться, чи провести?"

    main "Наче знаю."

    if main_gender == 0:
        main "Дякую вам. Тоді я побігла."
    elif main_gender == 1:
        main "Дякую вам. Тоді я побіг."
    elif main_gender == 2:
        main "Дякую вам. Тоді я побігли."

    main "До зустрічі."

    thon "Бувай-бувай!"

    py "Будь обережним на сходах."

    hide thon normal
    hide py normal

    "Ви швидко взяли сумку в руки і побігли на вихід. Навіть якщо черга не буде такою великою, як описала Пай, отримати швидше їжу Ви також не проти."

    scene bg corridor

    "Ви хутко пересуваєтесь коридорами, по можливості, не врізаючись в людей."

    scene black # TODO 6: add bg "їдальня"

    "Нарешті Ви в їдальні. Ви досить швидко прийшли, тому черга не дуже велика, але постояти доведеться."

    jump intro_java_and_js


label intro_java_and_js:
    "Потихеньку просуваучись в черзі, Ви слухаєте розмови студентів між собою."

    show stud1 at left
    show stud2
    show stud3 at right

    stud1 "Він якийсь ненормальний. Треба бути подалі від нього."

    stud2 "Він ще не відрахувався? Я думала його виженуть після того."

    stud1 "По спискам він все ще вчиться."

    stud3 "Не виженуть його, він же один з перших в рейтингу."

    stud1 "Він хоч зовнішність не змінив? А то не хочеться зустрітися з ним."

    stud2 "Не знаю, не бачила його ще і слава Богу."

    stud3 "А мені не повезло. Все такий самий: висока нахабна шпала. Ще й знову в костюмі ходить. Хто взагалі в унік в піджаку та брюках ходить?"

    stud2 "Може в нього немає іншого одягу. Ха-ха-ха."

    stud1 "Ха-ха, треба бути тихішими, а то ще почує і поб’є нас."

    stud3 "Головне каву його не чіпати, а на образи йому все одно. Сидить з кам'яним обличчям і мовчить. Може він не людина зовсім, а робот."

    stud1 "І не кава в нього, а солярка. Ха-ха-ха."

    "Студенти в черзі разом почали сміятися. Ті, хто в розмові не брав участь також тихенько посміювались."

    hide stud1
    hide stud2
    hide stud3

    "Отримавши нарешті їжу, Ви з підносом в руках відходите від черги. Озираючись навкруги, шукаєте вільний столик. Нарешті в самому кутку ви його знаходите і хутчіш йдете до нього."

    "Поставивши піднос на стіл, Ви сідаєте і починаєти їсти."

    show java normal

    "Через декілька секунд до вас підходить хлопець і сідає за стіл. Піднявши голову Ви бачите перед собою молоду людину в костюмі і стаканчиком кави."
    "Ви розумієте, що це сама та людина, про яку Ви чули не дочить гарні плітки, тому вирішуєте встати і пересісти за інший столик."

    "Хлопець з легким подивом дивиться на Ваші дії."

    boy1 "Чому ти йдеш? Більше місць немає. Не хвилюйся, ні я, ні ти один одному заважати не будемо."

    "Переконавшись, що Ви не зможете пересісти, Ви повертаєтесь на своє місце. Людина з пліток тихо попиває каву і ви, не порушуючи тиші, починаєте їсти."

    boy1 "А ти…"

    boy2 "Йоу! От ти де!"

    show java normal at left
    show js happy at right

    "Не давши договорити, з-за його спини з’являється хлопець і плескає нового знайомого по плечу. Через це на стіл проливається трохи кави. Легке здивування від неочікуваного привітання змінюється на стримувану злість."
    
    show java angry at left
    
    "Невже плітки були правдивими?"

    boy2 "Ти прикинь, я тебе по всьому корпусу шукав, а ти тут вже сидиш."
    boy2 "А хто це? Твій новий знайомий?"
    boy2 "То ти вже з першого дня друзів серед новачків шукаєш? Ніколи б про тебе такого не подумав, ха-ха!"

    "Здається, цей гучний хлопець зовсім не помічає, що він накоїв."

    boy1 "Ярик. Дивись."

    "Хлопець в костюмі перебиває Ярика і показує на стіл, де все ще виблискувала пролита кава."

    show js normal at right

    js "Ойй, Джава, ти як завжди. Ну пролилось трохи, ну що з того?"
    js "Тобі серветку дати? В мене є. І в тебе є, ти завжди їх з собою носиш."
    js "Ну що таке? Ти сильно образився? Хочеш, я тобі ще куплю."

    if main_gender == 0:
        js "Прада ж, емм.. Новенька?"
    elif main_gender == 1:
        js "Прада ж, емм.. Новенький?"
    elif main_gender == 2:
        js "Прада ж, емм.. Новенькі?"

    main "[main_name]."

    show js happy at right

    js "Добре, [main_name]. Я - Ярик, ну а ця обіжуля - Джава."

    if main_gender == 0:
        js "Ну так що, згодна зі мною?"
    elif main_gender == 1:
        js "Ну так що, згоден зі мною?"
    elif main_gender == 2:
        js "Ну так що, згодні зі мною?"

    js "Дивись, тут всього пара крапель, чого він так сердиться? Я б навіть уваги не звернув."

    menu:
        "Погодитись з Яриком?"
        
        "Так":
            main "Якщо чесно, я теж не бачу причини злитися. Небагато вилилось, тому легко прибрати, і загальний обсяг кави не постраждав."
           
            js "Оооот, бачиш. Все нормально ж. Не я один так думаю. Тому за більшістю правда."

            show java normal at left

            "Джава невдоволено хмикнув. Було видно, що він дійсно не радий всій цій ситуації. У той час як Ярик посміхався у всі 32 зуби і навіть не приховував радості, що Ви погодились з ним."

        "Ні":
            main "Якщо чесно, думаю, ти не дуже гарно поступив, Ярик. Дійсно, пролилось небагато, але так лякаючи можна і до нападу людину довести."
            
            show js angry at right

            js "Оййй, невже ти такий самий бурчун? Нічого ви, бумери, не розумієте. Це ж звичайний жарт для підняття настрою."

            show java happy at left

            "Джава ледве помітно посміхнувся. Здається, він радий, що Ви його підтримали. А от Ярик невдоволено щось почав бурчати під ніс. Здається, він і не думав, що Ви з ним не погодитесь."

    "Ви вирішуєте швидко прибрати краплі пролитої кави паперовими серветками, які Вам дали разом з підносом, щоб не посилювати конфлікт між цими двома."
    "Відчуття голоду дає про себе знати і, не звертаючи увагу на подальший діалог Джави і Ярика, продовжуєте свою трапезу."

    show js normal at right

    if main_gender == 0:
        js "Ладно, мала, пішли ми. У дорослих справи є. Весело з тобою було, наступного разу обов’язково даси мені свій номер. Па-па!"
    elif main_gender == 1:
        js "Ладно, малий, пішли ми. У дорослих справи є. Весело з тобою було, наступного разу обов’язково даси мені свій номер. Па-па!"
    elif main_gender == 2:
        js "Ладно, малі, пішли ми. У дорослих справи є. Весело з тобою було, наступного разу обов’язково даси мені свій номер. Па-па!"

    java "Дякую за компанію. Бувай."

    "З повним ротом їжі Ви змогли лише кивнути їм у слід. Таке відчуття, наче ураган пронесся. Ви згадуєте слова в натовпі про Джаву. Здається, не все було правдою, але каву він і правда сильно любить."

    "Ви швидко доїдаєте залишки страви. Після викиду сміття та поверненню підносу на місце, Ви за розкладом прямуєте до кабінету."

    scene bg corridor

    pause 1

    scene bg class

    pause 1

    "Новий предмет - новий викладач. Ви з нетерпінням чекаєте на нові знання."

    pause 2

    "Через кілька годин…"

    "От і закінчився Ваш перший навчальний день. Він був насиченим і цікавим, але повністю вичавив з Вас сили. Після закінчення останньої пари Ви вирішуєте зразу піти додому."

    scene bg corridor

    pause 1
    
    scene bg black # TODO 7: add bg

    pause 1

    scene bg park

    pause 1

    "По дорозі додому Ви згадуєте, як провели день. Вам сподобався перший навчальний день і нові знайомі, з якими Ви сьогодні бачили. Вдома Вас чекає Ваше перше домашнє завдання, а завтра обіцяє бути не менш насиченим за сьогодні."

    return