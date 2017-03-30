male(aaron).
male(duane).
male(edwin).

female(betty).
female(clara).
female(flora).

relation(aaron, betty).
relation(aaron, clara).
relation(betty, aaron).
relation(clara, aaron).
relation(betty, clara).
relation(clara, betty).
relation(flora, duane).
relation(flora, edwin).
relation(duane, flora).
relation(edwin, flora).
relation(duane, edwin).
relation(edwin, duane).

notRelation(flora, aaron).
notRelation(flora, betty).
notRelation(flora, clara).
notRelation(aaron, flora).
notRelation(betty, flora).
notRelation(clara, flora).
notRelation(duane, aaron).
notRelation(duane, betty).
notRelation(duane, clara).
notRelation(aaron, duane).
notRelation(betty, duane).
notRelation(clara, duane).
notRelation(edwin, aaron).
notRelation(edwin, betty).
notRelation(edwin, clara).
notRelation(aaron, edwin).
notRelation(betty, edwin).
notRelation(clara, edwin).

doctor(aaron).
doctor(betty).
doctor(duane).

lawyer(clara).
lawyer(edwin).
lawyer(flora).

solution(betty, duane).

related(K, V) :- % A
%killer_male(K, V) :- % A
	relation(K, V),
	not(K = V),
	male(K).

notRelated(K, V) :- % B
%killer_doctor(K, V) :- % B
	notRelation(K, V),
	not(K = V),
	doctor(K).

sameOccupation(K, V) :- % C
%victim_male(K, V) :- % C
	((doctor(K), doctor(V)); (lawyer(K), lawyer(V))),
	not(K = V),
	male(V).

diffOccupation(K, V) :- % D
%victim_female(K, V) :- % D
	((doctor(K), lawyer(V)); (lawyer(K), doctor(V))),
	not(K = V),
	female(V).

sameSex(K, V) :- % E
%killer_lawyer(K, V) :- % E
	((male(K), male(V)); (female(K), female(V))),
	not(K = V),
	lawyer(K).

diffSex(K, V) :- % F
%victim_doctor(K, V) :- % F
	((male(K), female(V)); (female(K), male(V))),
	not(K = V),
	doctor(V).
	
	
totallyNotTheSolutionButItActuallyIs(K, V) :-
	(notRelated(K, V), diffOccupation(K, V), diffSex(K, V));
	(notRelated(K, V), diffOccupation(K, V), sameSex(K, V));
	(notRelated(K, V), sameOccupation(K, V), diffSex(K, V));
	(notRelated(K, V), sameOccupation(K, V), sameSex(K, V));
	(related(K, V), diffOccupation(K, V), diffSex(K, V));
	(related(K, V), diffOccupation(K, V), sameSex(K, V));
	(related(K, V), sameOccupation(K, V), diffSex(K, V));
	(related(K, V), sameOccupation(K, V), sameSex(K, V)).
	
menu() :-
	writef("Clue A: is If the killer and the victim were related, the killer was a man.\n"),
	writef("To see pairings type 'related(K,V).' Keep hitting the space bar to see all the pairings\n\n"),

	writef("Clue B: If the killer and the victim were not related, the killer was a doctor.\n"),
	writef("To see pairings type 'notRelated(K,V).' Keep hitting the space bar to see all the pairings\n\n"),

	writef("Clue C: is If the killer and the victim had the same occupation, the victim was a man.\n"),
	writef("To see pairings type 'sameOccupation(K,V).' Keep hitting the space bar to see all the pairings\n\n"),

	writef("Clue D: If the killer and the victim had different occupations, the victim was a woman.\n"),
	writef("To see pairings type 'diffOccupation(K,V).' Keep hitting the space bar to see all the pairings\n\n"),

	writef("Clue E: If the killer and the victim were of the same sex, the killer was a lawyer.\n"),
	writef("To see pairings type 'sameSex(K,V).' Keep hitting the space bar to see all the pairings\n\n"),

	writef("Clue F: is If the killer and victim were different sexes, the victim was a doctor.\n"),
	writef("To see pairings type 'diffSex(K,V).' Keep hitting the space bar to see all the pairings\n\n"),
	
	writef("Type 'menu().' to see the clues again'\n\n"),
	
	writef("OR\n\n"),

	writef("To guess who the killer and the victim are type 'solution(Killer, Victim).' With the name of who you think the Killer is and who you think the Victim is in the correct spots i.e. solution(bill, bob)").