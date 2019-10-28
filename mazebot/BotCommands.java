package me.noelwiz.bots.mazebot;

import java.awt.Color;

import net.dv8tion.jda.core.entities.Message;
import net.dv8tion.jda.core.events.message.guild.GuildMessageReceivedEvent;
import net.dv8tion.jda.core.hooks.ListenerAdapter;

public class BotCommands extends ListenerAdapter{
	public static String trigger = "!!!";

	@Override
	public void onGuildMessageReceived(GuildMessageReceivedEvent event) {
		//every time a message is sent from a server, an event will be receved here
		Message incommingMessage = event.getMessage();
		String command[] = incommingMessage.getContentDisplay().split(" ");
		System.out.println(incommingMessage.getContentDisplay());

		
		//checking for trigger symbol
		if(!command[0].startsWith(trigger)) {
			//return now if not present
			return;
		} 
		
		//now we can still check for command text without hard codeing in the trigger, 
		//aka the trigger will still work if changed in Ref.java
		command[0] = command[0].substring(trigger.length());
		
		System.out.println("after trigger removal: "+command[0]);
		
		if(command[0].equalsIgnoreCase("command")) {
			incommingMessage.getChannel().sendMessage("command Triggered").queue();
			System.out.println("triggered by "+command[0]);
			return;
		}
		
	}
	

}
