from datapackage import Package

package = Package()
package.infer(r'C:\Users\USER\Desktop\Life_Project\Hosp_Amount\data\Hosp_piv.csv')
package.infer(r'C:\Users\USER\Desktop\Life_Project\Hosp_Amount\data\Hosp_anim.csv')
package.infer(r'C:\Users\USER\Desktop\Life_Project\Hosp_Amount\data\Hosp_fin.csv')
package.infer(r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\life_X_piv.csv')
package.infer(r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\anim.csv')
package.infer(r'C:\Users\USER\Desktop\Life_Project\Life_Expc\data\life_X_fin.csv')
package.commit()
package.save( r"C:\Users\USER\Desktop\Life_Project\datapackage.json")