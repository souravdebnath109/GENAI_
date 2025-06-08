from langchain.text_splitter import RecursiveCharacterTextSplitter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Correct download command
# nltk.download('punkt')
# nltk.download('punkt_tab')

# Sample text
text = """Bangladesh,[a] officially the People's Republic of Bangladesh,[b] is a country in South Asia. It is the eighth-most populous country in the world and among the most densely populated with a population of over 171 million within an area of 148,460 square kilometres (57,320 sq mi). Bangladesh shares land borders with India to the north, west, and east, and Myanmar to the southeast. It has a coastline along the Bay of Bengal to its south and is separated from Bhutan and Nepal by the Siliguri Corridor, and from China by the Indian state of Sikkim to its north. Dhaka, the capital and largest city, is the nation's political, financial, and cultural centre. Chittagong is the second-largest city and the busiest port of the country.

The territory of modern Bangladesh was a stronghold of many Buddhist and Hindu dynasties in ancient history. Following the Muslim conquest in 1204, the region saw Sultanate and Mughal rule.[15] During the Mughal period, particularly under the Bengal Subah, the region emerged as one of the most prosperous and commercially active parts of the empire, known for its thriving textile industry and agricultural productivity. The Battle of Plassey in 1757 marked the beginning of British colonial rule for the following two centuries. In the aftermath of the Partition of British India in 1947, East Bengal became the eastern and most populous wing of the newly formed Dominion of Pakistan and was later renamed to East Pakistan. Following over two decades of political repression and systematic racism from the West Pakistan-based government, East Pakistan experienced a civil war in 1971; ultimately leading to a war for independence. The Mukti Bahini, with assistance from Indian forces, waged a successful armed revolution; and at the expense of a genocide, Bangladesh became a sovereign nation on 16 December 1971. Post-Independence, Sheikh Mujibur Rahman led the country until his assassination in 1975. Presidency was later transferred to Ziaur Rahman, who himself was assassinated in 1981. The 1980s was dominated by the dictatorship of Hussain Muhammad Ershad, who was overthrown in a mass uprising in 1990. Following the democratisation in 1991, the "Battle of the Begums" between Khaleda Zia and Sheikh Hasina defined the country's politics for the next three decades. Hasina was overthrown in a student–led mass uprising in August 2024, and an interim government led by Nobel laureate Muhammad Yunus was formed.

Bangladesh is a unitary parliamentary republic based on the Westminster system. It is a middle power with the second-largest economy in South Asia. Bangladesh is home to the third-largest Muslim population in the world and the fifth-most spoken native language. It maintains the third-largest military in South Asia and is the largest contributor to the peacekeeping operations of the United Nations. It consists of eight divisions, 64 districts, and 495 sub-districts, and is home to the largest mangrove forest in the world. However, Bangladesh has one of the largest refugee populations in the world and continues to face challenges such as endemic corruption, lack of human rights, political instability, overpopulation, and adverse effects of climate change. It has twice chaired the Climate Vulnerable Forum and is a member of BIMSTEC, SAARC, OIC and the Commonwealth of Nations.

Etymology
Main article: Names of Bengal
The etymology of Bangladesh ("Bengali country") can be traced to the early 20th century, when Bengali patriotic songs, such as Aaji Bangladesher Hridoy by Rabindranath Tagore and Namo Namo Namo Bangladesh Momo by Kazi Nazrul Islam, used the term in 1905 and 1932 respectively.[16] Starting in the 1950s, Bengali nationalists used the term in political rallies in East Pakistan.

The term Bangla is a major name for both the Bengal region and the Bengali language. The origins of the term Bangla are unclear, with theories pointing to a Bronze Age proto-Dravidian tribe,[17] and the Iron Age Vanga Kingdom.[18] The earliest known usage of the term is the Nesari plate in 805 AD. The term Vangala Desa is found in 11th-century South Indian records.[19][20] The term gained official status during the Sultanate of Bengal in the 14th century.[21][22] Shamsuddin Ilyas Shah proclaimed himself as the first "Shah of Bangala" in 1342.[21] The word Bangāl became the most common name for the region during the Islamic period.[23] 16th-century historian Abu'l-Fazl ibn Mubarak mentions in his Ain-i-Akbari that the addition of the suffix "al" came from the fact that the ancient rajahs of the land raised mounds of earth in lowlands at the foot of the hills which were called "al".[24] This is also mentioned in Ghulam Husain Salim's Riyaz-us-Salatin.[25]

The Indo-Aryan suffix Desh is derived from the Sanskrit word deśha, which means "land" or "country". Hence, the name Bangladesh means "Land of Bengal" or "Country of Bengal".[20]

History
Main article: History of Bangladesh
Early history
The first great indigenous empire to cover the territory was the Mauryan Empire (ca. 320-180 B.C.). Following its decline, the kingdom of Samatata arose, which was a tributary state of the Gupta Empire (A.D. ca. 319-ca. 540). Harsha (A.D. 606–47) drew Samatata into its loosely administered political structure. Buddhist Pala Dynasty ruled the region from A.D. 750 to 1150. It was overthrown by the Hindu Sena dynasty, which ruled the territory until the Muslim conquests led by Muhammad Bakhtiyar Khalji of the Ghurid dynasty in 1204.[26]

Islamization and economic prosperity
Main articles: Bengal Sultanate and Bengal Subah

Murshid Quli Khan, the first independent Nawab of Bengal

Siraj ud-Daulah, the last independent Nawab of Bengal
Bengal was then incorporated into the Delhi Sultanate (A.D. 1206–1526).[27] In 1341, the independent Bengal Sultanate was established by Fakhruddin Mubarak Shah.[27] Amidst geographic expansion and economic prosperity, it was regarded by European and Chinese visitors as the "richest country to trade with".[28]: 10  The Mughal Empire conquered Bengal in 1576.[27] By the 18th century, the Bengal Subah emerged as the wealthiest province of the empire and was described as the "Paradise of Countries" and the "breadbasket of India".[27] Its citizens enjoyed some of the best standards of living in the world, as the region was a major global exporter and producer of cotton textiles (muslin in particular), silk and shipbuilding.[29]: 174  Following the decline of the Mughal Empire in the early 1700s, the region became a semi-independent state under the Nawabs of Bengal, founded by Murshid Quli Khan in 1717.

British colonial rule
Main article: Bengal Presidency
In 1757, the state led by Siraj-ud-Daulah was defeated by the British East India Company in the Battle of Plassey—which was key in establishing colonial British rule over Bengal and the wider Indian subcontinent. Bengal played a crucial role in the Industrial Revolution at the expense of an extraordinary capital flight and deindustrialization following British colonial loot and the collapse of the Bengali textile industry.[30][29]: 7–10  The catastrophic Great Bengal famine of 1770 caused over ten million deaths,[31] killing one-third of the total population of the Bengal Presidency,[32]: 47  and remains one of the deadliest man-made famines in history.

As a part of Pakistan
Main articles: Dominion of Pakistan, East Bengal, and East Pakistan
Further information: West Pakistan, Partition of Bengal (1947), and Partition of India
In the aftermath of direct British rule for nearly two centuries, the borders of modern Bangladesh were established with the partition of Bengal between India and Pakistan by the Radcliffe Line[33] during the partition of India on 15 August 1947, when the region became East Bengal as the eastern and most populous wing of the newly formed Dominion of Pakistan—alongside West Pakistan.[34] The western and eastern wings of the newly formed Pakistan were geographically separated by a distance of over 1,000 miles, which became the root cause of deep economic inequality.[35] Khawaja Nazimuddin was East Bengal's first chief minister with Frederick Chalmers Bourne its governor. The All Pakistan Awami Muslim League was formed in 1949. In 1950, the East Bengal Legislative Assembly enacted land reform, abolishing the Permanent Settlement and the zamindari system.[36] The Awami Muslim League was renamed as a more "secular" Awami League in 1953.[37] The first constituent assembly was dissolved in 1954. The United Front coalition swept aside the Muslim League in a landslide victory in the 1954 East Bengali legislative election. The following year, East Bengal was renamed East Pakistan as part of the One Unit programme, and the province became a vital part of the Southeast Asia Treaty Organization.

Amidst rising cultural and societal differences—the brutal government crackdown on the 1952 Bengali language movement to establish Bengali as the official language of Pakistan spurred Bengali nationalism and pro-democracy movements. Pakistan adopted a new constitution in 1956.[38] The Pakistan Armed Forces imposed martial law in 1958, following a coup d'état, with Ayub Khan establishing a dictatorship for over a decade. A new constitution was introduced in 1962, replacing the parliamentary system with a presidential and gubernatorial system (based on electoral college selection) known as "Basic Democracy".[39] In 1962, Dhaka became the seat of the National Assembly of Pakistan, a move seen as appeasing increased Bengali nationalism.[40] In 1966, Awami League leader Sheikh Mujibur Rahman announced a six-point movement for a federal parliamentary democracy.

Ethnic, linguistic, and cultural discrimination was common in Pakistan's civil and military services, in which Bengalis were under-represented;[41] leading to East Pakistan forging a distinct political identity.[42] Authorities banned Bengali literature and music in the state media.[43] The Pakistani government practised extensive economic discrimination against East Pakistan, including the refusal for foreign aid allocation.[44] Despite generating 70% of Pakistan's export revenue with jute and tea, East Pakistan received much less government spending. Notable economists from East Pakistan, including Rehman Sobhan and Nurul Islam demanded a separate foreign exchange account for the eastern wing, also pointing to the existence of two different economies within Pakistan itself, dubbed the Two-Economies Theory.[45][46] The populist leader Sheikh Mujibur Rahman was arrested for treason in the Agartala Conspiracy Case and was released during the 1969 uprising in East Pakistan which resulted in Ayub Khan's resignation. General Yahya Khan assumed power, reintroducing martial law.

A cyclone devastated the coast of East Pakistan in 1970, killing an estimated 500,000 people,[47] and the central government was criticised for its poor response.[48] After the December 1970 elections, the Bengali-nationalist Awami League won 167 of 169 East Pakistani seats in the National Assembly. The League claimed the right to form a government and develop a new constitution but was strongly opposed by the Pakistani military and the Pakistan Peoples Party (led by Zulfikar Ali Bhutto).

The 7 March Speech of Mujib led to a non-cooperation movement. The autocratic Pakistani government then initiated Operation Searchlight on 25 March 1971 in response.[49] Mujib signed the Proclamation of Independence on 26 March 1971, leading to the nine-month-long bloody liberation war, which led to a genocide,[50] and the culmination of Bangladesh as a sovereign nation following Pakistani surrender on 16 December 1971.

Independent Bangladesh
The Constitution of Bangladesh was enacted on November 4, 1972.[51] Following independence, the Mujib-led government engaged in large-scale corruption and mismanagement, leading to nationwide lawlessness and economic devastation. Efforts to establish one-party socialism and a large famine in 1974 led to Mujib's assassination in 1975 following a significant decline in his popularity.[52][53]: 131  The presidency was then transferred to Ziaur Rahman, who re-established public order, industrialized agriculture, founded the Bangladesh Nationalist Party (BNP) and initiated the creation of the South Asian Association for Regional Cooperation.[54] Following Rahman's assassination in 1981, the ensuing decade was a military dictatorship under Hussain Muhammad Ershad that saw infrastructural development, devolution reforms, privatization of nationalised industries and the declaration of Islam as the state religion in 1988.[55][56][57][58]

After the restoration of parliamentary democracy in 1991, power alternated between Khaleda Zia of the BNP and Sheikh Hasina of the Awami League, an era dubbed the "Battle of the Begums"—which defined Bangladesh's politics and history for next 34 years.[59][53]: 130  The return of the Awami League to power following a landslide victory in the 2008 general election[60] under Sheikh Hasina's leadership saw unprecedented economic progress alongside democratic backsliding, increasing authoritarianism, endemic corruption, and widespread human right abuses.[61] Hasina won her second, third and fourth consecutive terms in the 2014, 2018 and the 2024 general elections—all of which were shams and neither free nor fair.[62][63][64] Following a student-led mass uprising against the authoritarian government, Hasina was forced to resign and flee to India on 5 August 2024.[65] An interim government was formed on 8 August 2024, with Nobel laureate Muhammad Yunus as the Chief Adviser.[66]

Since the 1980s, driven by free market policies and economic liberalization measures, Bangladesh has achieved significant economic growth—emerging as one of the fastest-growing economies in the world, driven by its large textile industry, which is the second-largest in the world.[67] It has emerged as the second-largest economy in South Asia, surpassing the nominal GDP per capita of neighboring India.[68][69] Bangladesh has achieved remarkable feats in reducing its poverty rate, which has gone down from 80% in 1971,[70] to 44.2% in 1991,[71] and all the way down to 18.7% in 2022.[72] Its Human Development Index growth during the 21st century was surpassed only by China.[73] As part of the green transition, Bangladesh's industrial sector emerged as a leader in building green factories, with the country having the largest number of certified green factories in the world.[74] It has also given shelter to over a million Rohingya refugees fleeing the Rohingya genocide since 2017, which has strained its resources and highlighted its humanitarian commitments.[75]

Geography"""
# Step 1: Split into paragraphs
paragraph_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0,
    separators=["\n\n"]
)
paragraphs = paragraph_splitter.split_text(text)

# Step 2: Loop through Paragraphs → Sentences → Words
for para_index, para in enumerate(paragraphs):
    print(f"\n\n==== Paragraph {para_index + 1} ====")
    
    sentences = sent_tokenize(para)
    for sent_index, sent in enumerate(sentences):
        print(f"\n  Sentence {sent_index + 1}: {sent}")
        
        words = word_tokenize(sent)
        for word_index, word in enumerate(words):
            print(f"    Word {word_index + 1}: {word}")
