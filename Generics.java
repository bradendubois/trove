import java.util.Arrays;

abstract class PlayerBase {

    protected String name;

    protected PlayerBase(String name) {
        this.name = name;
    }
}

class NPC extends PlayerBase implements Comparable<NPC> {

    public NPC(String name) {
        super(name);
    }

    public int compareTo(NPC other) {
        return this.name.compareTo(other.name);
    }

    public String toString() {
        return "NPC: " + this.name;
    }
}

class HumanPlayer extends PlayerBase implements Comparable<HumanPlayer> {

    protected int level;

    public HumanPlayer(String name, int level) {
        super(name);
        this.level = level;
    }

    public int compareTo(HumanPlayer other) {
        return Integer.compare(this.level, other.level);
    }

    public String toString() {
        return "Player: " + this.name + ", Level: " + this.level;
    }
}

class Enemy extends PlayerBase implements Comparable<Enemy> {

    protected double dropLoot;

    public Enemy(String name, double dropLoot) {
        super(name);
        this.dropLoot = dropLoot;
    }

    public int compareTo(Enemy other) {
        return Double.compare(this.dropLoot, other.dropLoot);
    }

    public String toString() {
        return "Enemy: " + this.name + ", drops " + this.dropLoot + " gold.";
    }
}

class Boss extends PlayerBase implements Comparable<Boss> {

    protected int xp;

    public Boss(String name, int xp) {
        super(name);
        this.xp = xp;
    }

    public int compareTo(Boss other) {
        return Integer.compare(this.xp, other.xp);
    }

    public String toString() {
        return "Boss: " + this.name + ", drops " + this.xp + " xp.";
    }
}

class Array<T> {

    public T[] array;

    public Array(T... characters) {
        this.array = characters;
    }
}

public class Generics {

    public static void main(String[] args) {

        // NPCs
        NPC Lydia = new NPC("Lydia");
        NPC Aela = new NPC("Aela");
        NPC Farkas = new NPC("Farkas");
        NPC Vilkas = new NPC("Vilkas");
        NPC Njada = new NPC("Njada");

        // Human Players
        HumanPlayer Nadia = new HumanPlayer("Nadia", 49);
        HumanPlayer George = new HumanPlayer("George", 50);
        HumanPlayer Sneaky = new HumanPlayer("Sneaky", 37);
        HumanPlayer Splotch = new HumanPlayer("Splotch", 19);
        HumanPlayer LittleKitty = new HumanPlayer("Little Kitty", 24);

        // Enemies
        Enemy Draugr = new Enemy("Draugr", 140);
        Enemy BanditChief = new Enemy("Bandit Chief", 306);
        Enemy Necromancer = new Enemy("Necromancer", 220);
        Enemy DragonPriest = new Enemy("DragonPriest", 619);
        Enemy Hargraven = new Enemy("Hargraven", 957);

        // Bosses
        Boss Fjola = new Boss("Fjola", 2000);
        Boss LordHarkon = new Boss("Lord Harkon", 1250);
        Boss Karstaag = new Boss("Karstaag The Frost Giant", 3500);
        Boss Alduin = new Boss("Alduin", 8000);
        Boss Linwe = new Boss("Linwe", 7500);

        Array<NPC> NPCs = new Array<>(Lydia, Aela, Farkas, Vilkas, Njada);
        Array<HumanPlayer> Humans = new Array<>(Nadia, George, Sneaky, Splotch, LittleKitty);
        Array<Enemy> Enemies = new Array<>(Draugr, BanditChief, Necromancer, DragonPriest, Hargraven);
        Array<Boss> Bosses = new Array<>(Fjola, LordHarkon, Karstaag, Alduin, Linwe);


        // Sort them!
        Arrays.sort(NPCs.array);
        Arrays.sort(Humans.array);
        Arrays.sort(Enemies.array);
        Arrays.sort(Bosses.array);


        System.out.println("NPCs:");
        for (NPC npc : NPCs.array) {
            System.out.println(npc.toString());
        }

        System.out.println("\n\nHumans:");
        for (HumanPlayer human: Humans.array) {
            System.out.println(human.toString());
        }

        System.out.println("\n\nEnemies:");
        for (Enemy enemy : Enemies.array) {
            System.out.println(enemy.toString());
        }

        System.out.println("\n\nBosses:");
        for (Boss boss : Bosses.array) {
            System.out.println(boss.toString());
        }
    }
}