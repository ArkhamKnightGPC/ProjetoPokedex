CREATE TABLE pokemon(
    pokemon_id INT,
    nome VARCHAR(20) NOT NULL,
    altura INT, #em centimetros
    peso INT, #em gramas
    tipo1 VARCHAR(10) NOT NULL,
    tipo2 VARCHAR(10),
    fraqueza1 VARCHAR(10),
    fraqueza2 VARCHAR(10),
    fraqueza3 VARCHAR(10),
    fraqueza4 VARCHAR(10),
    evoluiDe int, #NULL se for pokemon basico
    PRIMARY KEY(pokemon_id)
);
INSERT INTO pokemon VALUES(1, 'Bulbasaur', 70, 6900, 'grama', 'venenoso', 'fogo', 'gelo', 'voador', 'psiquico', NULL);
INSERT INTO pokemon VALUES(2, 'Ivysaur', 100, 13000, 'grama', 'venenoso', 'fogo', 'gelo', 'voador', 'psiquico', 1);
INSERT INTO pokemon VALUES(3, 'Venusaur', 200, 100000, 'grama', 'venenoso', 'fogo', 'gelo', 'voador', 'psiquico', 2);
INSERT INTO pokemon VALUES(4, 'Charmander', 60, 8500, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(5, 'Charmeleon', 110, 19000, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, 4);
INSERT INTO pokemon VALUES(6, 'Charizard', 170, 90500, 'fogo', 'voador', 'agua', 'eletrico', 'pedra', NULL, 5);
INSERT INTO pokemon VALUES(7, 'Squirtle', 50, 9000, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(8, 'Wartortle', 100, 22500, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, 7);
INSERT INTO pokemon VALUES(9, 'Blastoise', 160, 100000, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, 8);
INSERT INTO pokemon VALUES(10, 'Caterpie', 30, 2900, 'inseto', NULL, 'fogo', 'voador', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(11, 'Metapod', 70, 9900, 'inseto', NULL, 'fogo', 'voador', 'pedra', NULL, 10);
INSERT INTO pokemon VALUES(12, 'Buterfree', 110, 32000, 'inseto', 'voador', 'fogo', 'voador', 'eletrico', 'gelo', 11);
INSERT INTO pokemon VALUES(13, 'Weedle', 30, 3200, 'inseto', 'venenoso', 'fogo', 'psiquico', 'voador', 'pedra', NULL);
INSERT INTO pokemon VALUES(14, 'Kakuna', 60, 10000, 'inseto', 'venenoso', 'fogo', 'psiquico', 'voador', 'pedra', 13);
INSERT INTO pokemon VALUES(15, 'Beedrill', 100, 29500, 'inseto', 'venenoso', 'fogo', 'psiquico', 'voador', 'pedra', 14);
INSERT INTO pokemon VALUES(16, 'Pidgey', 30, 1800, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(17, 'Pidgeotto', 110, 30000, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, 16);
INSERT INTO pokemon VALUES(18, 'Pidgeot', 150, 39500, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, 17);
INSERT INTO pokemon VALUES(19, 'Rattata', 30, 3500, 'normal', NULL, 'lutador', NULL, NULL, NULL, NULL);
INSERT INTO pokemon VALUES(20, 'Raticate', 70, 18500, 'normal', NULL, 'lutador', NULL, NULL, NULL, 19);
INSERT INTO pokemon VALUES(21, 'Spearow', 30, 2000, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(22, 'Fearow', 120, 38000, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, 21);
INSERT INTO pokemon VALUES(23, 'Ekans', 200, 6900, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(24, 'Arbok', 350, 65000, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, 23);
INSERT INTO pokemon VALUES(25, 'Pikachu', 40, 6000, 'eletrico', NULL, 'terra', NULL, NULL, NULL, NULL);
INSERT INTO pokemon VALUES(26, 'Raichu', 80, 30000, 'eletrico', NULL, 'terra', NULL, NULL, NULL, 25);
INSERT INTO pokemon VALUES(27, 'Sandshrew', 60, 12000, 'terra', NULL, 'agua', 'grama', 'gelo', NULL, NULL);
INSERT INTO pokemon VALUES(28, 'Sandslash', 100, 29500, 'terra', NULL, 'agua', 'grama', 'gelo', NULL, 27);
INSERT INTO pokemon VALUES(29, 'Nidoran', 40, 700, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(30, 'Nidorina', 80, 20000, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, 29);
INSERT INTO pokemon VALUES(31, 'Nidoqueen', 130, 60000, 'venenoso', 'terra', 'agua', 'psiquico', 'gelo', 'terra', 30);
INSERT INTO pokemon VALUES(32, 'Nidoran', 50, 9000 , 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(33, 'Nidorino', 90, 19500 , 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, 32);
INSERT INTO pokemon VALUES(34, 'Nidoking', 140, 62000, 'venenoso', 'terra', 'agua', 'psiquico', 'gelo', 'terra', 33);
INSERT INTO pokemon VALUES(35, 'Clefairy', 60, 7500, 'fada', NULL, 'metal', 'venenoso', NULL, NULL, NULL); # evolui do 173
INSERT INTO pokemon VALUES(36, 'Clefable', 130, 40000, 'fada', NULL, 'metal', 'venenoso', NULL, NULL, 35);
INSERT INTO pokemon VALUES(37, 'Vulpix', 60, 9900, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(38, 'Ninetales', 110, 19900, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, 37);
INSERT INTO pokemon VALUES(39, 'Jigglypuff', 50, 5500, 'normal', 'fada', 'metal', 'venenoso', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(40, 'Wigglytuff', 100, 12000, 'normal', 'fada', 'metal', 'venenoso', NULL, NULL, 39);
INSERT INTO pokemon VALUES(41, 'Zubat', 80, 7500, 'venenoso', 'voador', 'fisico', 'eletrico', 'gelo', 'pedra', NULL);
INSERT INTO pokemon VALUES(42, 'Golbat', 160, 55000, 'venenoso', 'voador', 'fisico', 'eletrico', 'gelo', 'pedra', 41);
INSERT INTO pokemon VALUES(43, 'Oddish', 50, 5400, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', NULL);
INSERT INTO pokemon VALUES(44, 'Gloom', 80, 8600, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', 43);
INSERT INTO pokemon VALUES(45, 'Vileplume', 120, 18600, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', 44);
INSERT INTO pokemon VALUES(46, 'Paras', 30, 5400, 'inseto', 'grama', 'fogo', 'voador', 'gelo', 'venenoso', NULL);
INSERT INTO pokemon VALUES(47, 'Parasect', 100, 29500, 'inseto', 'grama', 'fogo', 'voador', 'gelo', 'venenoso', 47);
INSERT INTO pokemon VALUES(48, 'Venonat', 100, 30000, 'inseto', 'venenoso', 'fogo', 'psiquico', 'voador', 'pedra', NULL);
INSERT INTO pokemon VALUES(49, 'Venomoth', 150, 12500, 'inseto', 'venenoso', 'fogo', 'psiquico', 'voador', 'pedra', 48);
INSERT INTO pokemon VALUES(50, 'Diglett', 20, 800, 'terra', NULL, 'agua', 'grama', 'gelo', NULL, NULL);
INSERT INTO pokemon VALUES(51, 'Dugtrio', 70, 33300, 'terra', NULL, 'agua', 'grama', 'gelo', NULL, 50);
INSERT INTO pokemon VALUES(52, 'Meowth', 40, 4200, 'normal', NULL, 'lutador', NULL, NULL, NULL, NULL);
INSERT INTO pokemon VALUES(53, 'Persian', 100, 3200, 'normal', NULL, 'lutador', NULL, NULL, NULL, 53);
INSERT INTO pokemon VALUES(54, 'Psyduck', 80, 19600, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(55, 'Golduck', 170, 76600, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, 54);
INSERT INTO pokemon VALUES(56, 'Mankey', 50, 28000, 'lutador', NULL, 'psiquico', 'voador', 'fada', NULL, NULL);
INSERT INTO pokemon VALUES(57, 'Primeape', 100, 32000, 'lutador', NULL, 'psiquico', 'voador', 'fada', NULL, 56);
INSERT INTO pokemon VALUES(58, 'Growlithe', 70, 19000, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(59, 'Arcanine', 190, 155000, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, 58);
INSERT INTO pokemon VALUES(60, 'Poliwag', 60, 12400, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(61, 'Poliwhirl', 100, 20000, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(62, 'Poliwrath', 130, 54000, 'agua', 'lutador', 'fada', 'grama', 'voador', 'psiquico', 61);        # falta fraqueza
INSERT INTO pokemon VALUES(63, 'Abra', 90, 19500, 'psiquico', NULL, 'fantasma', 'sombrio', 'inseto', NULL, NULL); 
INSERT INTO pokemon VALUES(64, 'Kadabra', 130, 56500, 'psiquico', 'fantasma', 'sombrio', 'inseto', NULL, NULL, 63);
INSERT INTO pokemon VALUES(65, 'Alakazam', 150, 48000, 'psiquico', 'fantasma', 'sombrio', 'inseto', NULL, NULL, 64);
INSERT INTO pokemon VALUES(66, 'Machop', 80, 19500, 'lutador', NULL, 'psiquico', 'voador', 'fada', NULL, NULL);
INSERT INTO pokemon VALUES(67, 'Machoke', 150, 70500, 'lutador', NULL, 'psiquico', 'voador', 'fada', NULL, 66);
INSERT INTO pokemon VALUES(68, 'Machamp', 160, 130000, 'lutador', NULL, 'psiquico', 'voador', 'fada', NULL, 67);
INSERT INTO pokemon VALUES(69, 'Belsprout', 70, 4000, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', NULL);
INSERT INTO pokemon VALUES(70, 'Weepinbell', 100, 6400, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', 69);
INSERT INTO pokemon VALUES(71, 'Vectreebel', 170, 15500, 'grama', 'venenoso', 'fogo', 'psiquico', 'voador', 'gelo', 70);
INSERT INTO pokemon VALUES(72, 'Tentacool', 90, 45500, 'agua', 'venenoso', 'psiquico', 'eletrico', 'terra', NULL, NULL);
INSERT INTO pokemon VALUES(73, 'Tentacruel', 160, 55000, 'agua', 'venenoso', 'psiquico', 'eletrico', 'terra', NULL, 72);
INSERT INTO pokemon VALUES(74, 'Geodude', 40, 20000, 'pedra', 'terra', 'grama', 'agua', 'terra', 'lutador', NULL);            # falta fraqueza
INSERT INTO pokemon VALUES(75, 'Graveler', 100, 105000, 'pedra', 'terra', 'grama', 'agua', 'terra', 'lutador', 74);           # falta fraqueza 
INSERT INTO pokemon VALUES(76, 'Golem', 140, 300000, 'pedra', 'terra', 'grama', 'agua', 'terra', 'lutador', 75);              # falta fraqueza
INSERT INTO pokemon VALUES(77, 'Ponyta', 100, 30000, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(78, 'Rapidash', 170, 95000, 'fogo', NULL, 'agua', 'terra', 'pedra', NULL, 77);
INSERT INTO pokemon VALUES(79, 'Slowpoke', 120, 36000, 'agua', 'psiquico', 'fantasma', 'sombrio', 'grama', 'eletrico', NULL); # falta fraqueza
INSERT INTO pokemon VALUES(80, 'Slowbro', 160, 78500, 'agua', 'psiquico', 'fantasma', 'sombrio', 'grama', 'eletrico', 79);    # falta fraqueza
INSERT INTO pokemon VALUES(81, 'Magnemite', 30, 6000, 'eletrico', 'aco', 'fogo', 'lutador', 'terra', NULL, NULL);
INSERT INTO pokemon VALUES(82, 'Magneton', 100, 60000, 'eletrico', 'aco', 'fogo', 'lutador', 'terra', NULL, 81);
INSERT INTO pokemon VALUES(83, 'Farfetchd', 80, 15000, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(84, 'Doduo', 140, 39200, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, NULL);
INSERT INTO pokemon VALUES(85, 'Dodrio', 180, 85200, 'normal', 'voador', 'eletrico', 'gelo', 'pedra', NULL, 84);
INSERT INTO pokemon VALUES(86, 'Seel', 110, 90000, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(87, 'Dewgong', 170, 120000, 'agua', 'gelo', 'grama', 'eletrico', 'lutador', 'pedra', 86);
INSERT INTO pokemon VALUES(88, 'Grimer', 90, 30000, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, NULL);
INSERT INTO pokemon VALUES(89, 'Muk', 120, 30000, 'venenoso', NULL, 'psiquico', 'terra', NULL, NULL, 88);
INSERT INTO pokemon VALUES(90, 'Shellder', 30, 4000, 'agua', NULL, 'grama', 'eletrico', NULL, NULL, NULL);
