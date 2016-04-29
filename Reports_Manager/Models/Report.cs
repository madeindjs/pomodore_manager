using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Data.SqlClient;
using System.Linq;
using System.Web; 

namespace Reports_Manager.Models
{
    public class Report
    {
        [Key]
        public int Id { get; set; }
        [Required]
        public int User_id { get; set; }
        [Required]
        public string Shop_otp { get; set; }
        public string Serie { get; set; }
        public int? Categoriy_id { get; set; }
        public DateTime? Created_at { get; set; }
        public DateTime? Updated_at { get; set; }
        public string Asked_by { get; set; }
        public string Notes { get; set; }
        public TimeSpan? T_spend { get; set; }
        public TimeSpan? T_travel { get; set; }
        public TimeSpan? T_plus { get; set; }
        public string Description { get; set; }
        public string Analysis { get; set; }
        public string Facts { get; set; }
        public string Forecast { get; set; }

        public virtual User User { get; set; }
        public virtual Shop Shop { get; set; }
        public virtual List<Shop> Cabinets { get; set; }


        public void get_user()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            System.Data.Entity.DbSet<User> database_users = database.Users;
            User = database_users.First(user => user.Id == this.User_id);
        }

        public void get_shop()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            System.Data.Entity.DbSet<Shop> database_shops = database.Shops;
            Shop = database_shops.First(shop => shop.Otp == Shop_otp);
        }

        public void get_cabinets()
        {
            CarrierDataEntities database = new CarrierDataEntities();
            System.Data.Entity.DbSet<Shop> database_shops = database.Shops;
            string[] separators = { "_" };
            string[] serial_numbers = Serie.Split( separators , StringSplitOptions.RemoveEmptyEntries );
            foreach(string serial_number in serial_numbers)
            {
                Cabinets.Add(database_shops.First(shop => shop.Serie == serial_number));
            }
        }


        public Boolean save()
        {
            SqlConnection sqlConnection = new SqlConnection("Data Source=AH734716\\SQLEXPRESS;Initial Catalog=Reports_Manager.Models.CarrierDataEntities;Integrated Security=True");

            try
            {
                sqlConnection.Open();

                string sqlCommand_str = String.Format(
                    "INSERT INTO [Reports] (User_id, Serie, Shop_otp , T_spend , T_travel , T_plus, Categoriy_id , Description , Asked_by , Analysis , Facts , Forecast , Notes , Updated_at )" +
                    " VALUES ('{0}' , '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{11}', '{12}' , GETDATE()  );",
                    User_id, Serie, Shop_otp, T_spend, T_travel, T_plus, Categoriy_id , Description, Asked_by, Analysis, Facts, Forecast, Notes);

                SqlCommand sqlCommand = new SqlCommand(sqlCommand_str, sqlConnection);

                sqlCommand.ExecuteNonQuery();

            }
            catch (Exception e)
            {
                System.Diagnostics.Debug.WriteLine(e.Message);
                return false;
            }
            finally
            {
                sqlConnection.Close();
            }
            return true;
        }

    }
}