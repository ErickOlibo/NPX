"""This module create random Entries for the Database to facilitate GUI creation."""
import random
import datetime
from helpers import EntriesData


class DataSampler:

    def _get_entry_data(self) -> EntriesData:
        user = random.choice(self.usernames).lower()
        title = random.choice(self.phrases)
        text = " ".join(random.choices(self.phrases, k=random.randint(5, 15)))
        (rdn_day, rdn_time) = self._get_random_date_time()
        tags = ", ".join(random.choices(self.tags, k=random.randint(2, 4)))
        return EntriesData(user, title, text, rdn_day, rdn_time, tags)

    def _get_random_date_time(self) -> tuple[str, str]:
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=90)
        random_date = start_date + (end_date - start_date) * random.random()
        chosen_day = random_date.strftime('%Y/%m/%d')
        chosen_time = random_date.strftime("%H:%M:%S")
        return (chosen_day, chosen_time)

    def get_sample(self, size: int) -> list[EntriesData]:
        return [self._get_entry_data() for _ in range(size)]

    usernames = ["Anne-Claire", "Erick", "Fiona", "Ibrahim", "Michaelia", "Moritz"]

    tags = [
        "Abusive", "Alone", "Alzheimers", "Angry", "Anti-social", "Asylums",
        "Attention seekers", "Autism", "Bewildered", "Bimbo", "Bonkers", "Brain damage",
        "Brain dead", "Breakdown", "Childish", "Cola sweat", "Confused", "Crackers",
        "Crazy", "Cushioned walks", "Dangerous", "Deformed", "Demanding", "Demented",
        "Depressed", "Depression", "Deranged", "Difficulty learning", "Dinlo", "Disabled",
        "Disarmed", "Disorientated", "Distorted", "Distressed", "Distressing", "Disturbed",
        "Disturbing", "Disturbing images", "Div", "Dizzy", "Doctors", "Dofuss", "Dopy", "Downy",
        "Dribbling", "Drugged-up", "Dulally", "Dumb", "Embarrassed", "Embarrassing", "Empty",
        "Escaped from an asylum", "Excluded", "Feel sorry", "Flid", "Flip in the head",
        "Freak", "Fruit cake", "Frustrated", "Frustrating", "Frustration", "Fucked",
        "Funny", "Gay", "Get lost", "Gone in the head", "Goon", "Green room", "Halfwit",
        "Hallucinating", "Hallucinations", "Hand fed", "Handicapped", "Happy club",
        "Hard", "Hard work", "Head banging", "Head case", "Helpless", "Hurting yourself",
        "Idiot", "Ill", "Indecisive", "Infixed in bad habits", "Insane", "Insecure",
        "Intellectually challenged", "Intimidating", "Irrational", "Isolated",
        "Joe from Eastenders", "Jumpy", "Learning difficulties", "Loneliness",
        "Lonely", "Loony", "Loony bin", "Loser", "Lost", "Lunatic", "M.E.", "Mad",
        "Made fun of", "Madness", "Manic depression", "Mass murderers", "Mental",
        "Mental hospital", "Mental illness", "Mental institution", "Mentally challenged",
        "Mentally handicapped", "Mentally ill", "Misunderstood", "Mong", "Muppets", "Needing help",
        "Nervous", "Nightmares", "No-one upstairs", "Non-caring", "None caring", "Not all there",
        "Not fair", "Not happy", "Not obvious", "Not quite there", "Numscull", "Nutcase", "Nuts",
        "Nutter", "Nutty as a fruitcake", "OCD", "Odd", "Oddball", "Off their rocker", "Out of it",
        "Outcast", "Padded cells", "Paedophile", "Panicked", "Paranoid", "Patch Adams",
        "People who are obsessed", "Perfectly normal", "Perverted", "Physical problems", "Physically ill",
        "Pills", "Pinflump", "Pive", "Plank", "Ponce", "Pressure", "Pressurising families",
        "Problems", "Psychiatric", "Psychiatric health", "Psychiatrist", "Psycho", "Psychopath",
        "Reject", "Retard", "Sad", "Scared", "Scary", "Schizo", "Schizophrenia", "Schizophrenic",
        "School can cause it", "School pressure", "Screw Loose", "Screwed", "Segregation", "Self-harm",
        "Shock syndrome", "Shouts", "Sick in the head", "Simple", "Simpleton", "Spakka", "Spanner",
        "Spastic", "Spaz", "Split personality", "Spoone", "Stiggy nutter", "Stigma", "Strait jackets",
        "Strange", "Stress", "Stressed", "Therapist", "Therapy", "Thick", "Thicko", "Thicky", "Tiring",
        "Too much pressure", "Touchy to talk to", "Troubled", "Twisted", "Twister", "Ugly",
        "Unable to make decisions", "Unappreciated", "Unapproachable", "Uncomfortable",
        "Under pressure", "Understandable", "Unfair", "Unfortunate", "Unhappy", "Unpredictable",
        "Unstable", "Upsetting", "Veg", "Vegetable", "Victim", "Victimised", "Violence", "Violent",
        "Voices", "Voices in your head", "Vulnerable", "Wacky", "Wally", "War", "Weird", "Weirdo",
        "Wheel chairs", "Wheelchair jockey", "Wheelchairs", "White coats", "Wild", "Wild funny noises",
        "Window licker", "Withdrawn", "World of their own", "Worried", "You belong in a home"]

    phrases = [
        "Everything you can imagine is real.",
        "Live as if you were to die tomorrow.",
        "It always seems impossible until it's done.",
        "The time is always right to do what is right.",
        "Happiness depends upon ourselves.",
        "Because you are alive, everything is possible.",
        "Our truest life is when we are in dreams awake.",
        "A warm smile is the universal language of kindness.",
        "Simplicity is the ultimate sophistication.",
        "Love yourself first and everything else falls into line.",
        "Lead from the heart, not the head.",
        "Life is like riding a bicycle. To keep your balance, you must keep moving.",
        "It is never too late to be what you might have been.",
        "Growth begins when we start to accept our own weakness.",
        "The real difficulty is to overcome how you think about yourself.",
        "I have never been hurt by what I have not said.",
        "I like criticism. It makes you strong.",
        "Decisions without actions are worthless.",
        "Dream as if you'll live forever, live as if you'll die today.",
        "Oh, the things you can find, if you don't stay behind.",
        "Be so good they can't ignore you. ",
        "If you tell the truth you don't have to remember anything.",
        "I don't need it to be easy, I need it to be worth it.",
        "To live will be an awfully big adventure.",
        "There is no substitute for hard work.",
        "Never let your emotions overpower your intelligence.",
        "Turn your wounds into wisdom.",
        "It hurt because it mattered.",
        "I have nothing to lose but something to gain.",
        "A happy soul is the best shield for a cruel world.",
        "Let the beauty of what you love be what you do.",
        "Whatever you do, do it well.",
        "Every moment is a fresh beginning.",
        "The simplest things are often the truest.",
        "Happiness is nothing more than good health and a bad memory.",
        "The biggest asset in the world is your mindset.",
        "Either you run the day or the day runs you.",
        "Learn to live with less so that you appreciate more.",
        "Happiness is not something ready-made. It comes from your own actions.",
        "Learning is a weightless treasure you can always carry easily.",
        "You must expect great things of yourself before you can do them.",
        "Laugh as much as you breathe and love as long as you live.",
        "If I'm gonna tell a real story, I'm gonna start with my name.",
        "Change the world by being yourself.",
        "Tomorrow is now.",
        "Mistakes are proof that you are trying.",
        "I live a beautiful life with fewer things—simple, yet full.",
        "Things work out best for those who make the best of how things work out.",
        "Stay hungry, stay foolish.",
        "What will you do with your one wild and precious life?",
        "The best things in life aren't things.",
        "The first step in crafting the life you want is to get rid of everything you don't."]


if __name__ == "__main__":
    sampler = DataSampler()
    sample = sampler.get_sample(10)

    for element in sample:
        print(element)
