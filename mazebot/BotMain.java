package me.noelwiz.bots.mazebot;

import javax.security.auth.login.LoginException;

import net.dv8tion.jda.core.AccountType;
import net.dv8tion.jda.core.JDA;
import net.dv8tion.jda.core.JDABuilder;
import net.dv8tion.jda.core.entities.Game;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

public class BotMain extends ListenerAdapter {
	public static JDA api;
	
	public static void main(String[] args) {
		//read any files if we want to test implimenting a text file for set up
		//theory: set up class people can run to make the .txt file that would be read here
		
		try {
			//logs in
			api = new JDABuilder(AccountType.BOT).setToken("bot token goes here").buildBlocking();
			//updates currently playing
			api.getPresence().setGame(Game.of(Game.GameType.DEFAULT, "With Mazes"));
			api.addEventListener(new BotCommands());
		} catch (LoginException | IllegalArgumentException | InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
